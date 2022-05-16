# Timetracker

<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

Create quick and short daily summaries of your Toggl entries per project per description.

## Usage

You would need python version 3.6 or above. You can check your current version by running `python3 -V`

You will need to generate a Toggl API token which can be found at the bottom of the page of your [Toggl profile](https://track.toggl.com/app/profile).

Install the dependencies then run the script. If date options are not provided, timetracker will only summarize entries for today.

```bash
$ pip install -r requirements.txt
$ python3 timetracker.py --since 2020-01-01 --token <toggle_token>

checkin 2020-01-01
- 3.64 hrs #project-1 Bugs
- 1.07 hrs #project-2 Features
- 0.50 hr #project-2 Pull Requests
```

The following date options are available:

- `--since {yyyy-mm-dd}`
- `-y` / `--yesterday`
- `-w` / `--week`
- `-l` / `--lastweek`

You can also set the env variable `TIMETRACKER_TOKEN` and skip the token arg

```bash
export TIMETRACKER_TOKEN=<toggl_token>
python3 timetracker.py --since 2020-01-01
```

You can also set the timezone. The default value is `Asia/Manila`

```bash
python3 timetracker.py --since 2020-01-01 --timezone='Asia/Manila'
```

The script applies `.lower()` to the project name and adds `#` in front of the project. `Project-1` will be converted to `#project-1`

## Development

Setting up development

```bash
pre-commit install
```

## TODO

- [ ] Project format
- [ ] Add some logging
- [ ] Set up ci/cd
