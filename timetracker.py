import os
from datetime import datetime, timedelta
from toolz import groupby

import pytz
import requests
from requests.auth import HTTPBasicAuth


def main(token, date=None):
    entries = get_entries(date, token)
    projects = get_projects(entries, token)
    summary = summarize(entries, projects)
    return gen_report(summary)


def get_entries(date, token):
    now = datetime.now(pytz.timezone("Asia/Manila"))
    start_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
    start_date = start_date - timedelta(days=1)
    end_date = start_date + timedelta(days=1)
    entries = requests.get(
        "https://www.toggl.com/api/v8/time_entries",
        params={"start_date": start_date.isoformat(), "end_date": end_date.isoformat()},
        auth=HTTPBasicAuth(token, "api_token"),
    ).json()
    return entries


def get_projects(entries, token):
    project_ids = {e.get("pid") for e in entries if e.get("pid") is not None}
    projects_info = {pid: get_project_by_id(pid, token=token) for pid in project_ids}
    projects = {k: v["name"] for k, v in projects_info.items()}
    return projects


def get_project_by_id(id, token):
    project = requests.get(
        f"https://www.toggl.com/api/v8/projects/{id}",
        auth=HTTPBasicAuth(token, "api_token"),
    )
    return project.json().get("data")


def summarize(entries, projects):
    def _summarize(vals):
        summary = {
            k: sum(map(lambda i: i["duration"], v))
            for k, v in groupby(seq=vals, key=lambda x: x["description"]).items()
        }
        return summary

    summary = {
        projects.get(k): _summarize(v)
        for k, v in groupby(seq=entries, key=lambda x: x.get("pid")).items()
        if k is not None
    }
    return summary


def gen_report(summary):
    r = """checkin\n"""
    for project, entries in summary.items():
        for description, time in entries.items():
            if time < 0:
                print(
                    f"WARN: Got negative time for {description}. Mostly there is a running timer"
                )
            r += f"- {time/3600:.2f} {'hrs' if time>1.0 else 'hr'} #{project.lower()} {description}\n"
    return r


if "__main__" == __name__:
    token = os.getenv("TOGGL_TOKEN", None)
    if token is None:
        raise ValueError("Need environment variable TOGGL_TOKEN")
    summary = main(token)
    print("\n")
    print(summary)
