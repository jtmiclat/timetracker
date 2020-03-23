import click
import pendulum
import requests
from requests.auth import HTTPBasicAuth
from toolz import groupby, valmap


def get_entries(token, start):
    start_date = start.set(hour=0, minute=0, second=0, microsecond=0)
    entries = requests.get(
        "https://www.toggl.com/api/v8/time_entries",
        params={"start_date": start_date.isoformat()},
        auth=HTTPBasicAuth(token, "api_token"),
    ).json()
    return entries


def get_projects(token, entries):
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


def summarize(entries, projects, timezone):
    mod_entries = [
        {
            "date": pendulum.parse(e["start"])
            .in_timezone(timezone)
            .format("YYYY-MM-DD"),
            **e,
        }
        for e in entries
    ]
    summary = valmap(
        lambda e: sum(map(lambda i: i["duration"], e)),
        groupby(
            key=lambda x: (x["date"], x.get("pid"), x["description"]), seq=mod_entries
        ),
    )
    formated_summaries = [
        {
            "date": k[0],
            "project": projects.get(k[1]),
            "description": k[2],
            "duration": v,
        }
        for k, v in summary.items()
    ]
    return groupby("date", formated_summaries)


def format_report(date, summary):
    r = f"checkin {date}\n"
    for entry in summary:
        project = entry["project"] if entry["project"] else "no-project"
        description = entry["description"]
        duration_hrs = entry["duration"] / 3600
        if duration_hrs < 0:
            print(
                f"WARN: Got negative time for {description}. There might be a running timer"
            )
        r += f"- {duration_hrs:.2f} {'hrs' if duration_hrs>1.0 else 'hr'} #{project.lower()} {description}\n"
    return r


@click.command()
@click.option("--since", type=str)
@click.option("--token", type=str)
@click.option("--timezone", type=str, default="Asia/Manila")
def main(since, token, timezone):
    if token is None or token == "":
        raise ValueError("Token variable is needed")
    now = pendulum.now(timezone)
    if since:
        start = pendulum.parse(since).set(tz=timezone)
    else:
        start = now
    entries = get_entries(token, start)
    projects = get_projects(token, entries)
    summaries = summarize(entries, projects, timezone)
    for date, summary in summaries.items():
        print(format_report(date, summary))


if "__main__" == __name__:
    main(auto_envvar_prefix="TIMETRACKER")
