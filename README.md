# Timetracker

<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

Create quick and short daily summaries of your toggl entries per project per description.

## Usage

You would need pythhon with a version 3.6 or above. You can check by running `python3 -V`

You first need to generate Toggl API token which can be found in youor [profile](https://toggl.com/app/profile)  at the botom of the page.

Install then run the script. If no `--since` is given, will summarize only today.

```bash
pip install -r requirements.txt
python3 timetracker.py --since 2020-01-01 --token <toggle_token>
```

You can also set env variable `TIMETRACKER_TOKEN` to the `toggle_token` and you can skip
the token arg
```
python3 timetracker.py --since 2020-01-01
```

## Development
Setting up development

```bash
pre-commit install
```

## TODO

- [ ] Add some logging
- [ ] Set up ci/cd
