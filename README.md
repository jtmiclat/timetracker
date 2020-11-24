# Timetracker

<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

Create quick and short daily summaries of your toggl entries per project per description.

## Usage

You would need python version 3.6 or above. You can check your current version by running `python3 -V`

You will need to generate Toggl API token which can be found at the bottom of the page of your [Toggl profile](https://track.toggl.com/app/profile).

Install the dependencies then run the script. If `--since` is not provided, timetracker will only summarize entries for today.

```bash
$ pip install -r requirements.txt
$ python3 timetracker.py --since 2020-01-01 --token <toggle_token>

checkin 2020-01-01
- 3.64 hrs #project-1 Bugs
- 1.07 hrs #project-2 Features
- 0.50 hr #project-2 Pull Requests
```

You can also set env variable `TIMETRACKER_TOKEN` to the `token` and you can skip
the token arg
```
export TIMETRACKER_TOKEN=<toggl_token>
python3 timetracker.py --since 2020-01-01
```

You can also set the timezone. The default value is `Asia/Manila`
```
python3 timetracker.py --since 2020-01-01 --timezone='Asia/Manila'
```

The script applies a `.lower()` to the the project name and places a `#` infront of the project. `Project-1` will be converted to `#project-1`

## Development
Setting up development

```bash
pre-commit install
```

## TODO
- [ ] Project format
- [ ] Add some logging
- [ ] Set up ci/cd
