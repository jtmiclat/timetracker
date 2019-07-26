# Time-tracker

<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

Create quick and short daily summaries of your toggl entries per project per description.

## Usage
Build docker image and run the following

```bash
docker run -e TOGGL_TOKEM=<token> jtmiclat/time-tracker
```

## Development
Setting up development

```bash
pip install -r requirements.txt requirements-dev.txt
pre-commit install
```

## TODO

- [ ] Figure out timezones
- [ ] Add Docuemntaiton clean up code
- [ ] Add some logging
- [ ] Set up ci/cd
