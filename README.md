# flask-api-template

## Features

- [x] Flask API definition with GET/POST routes
- [x] Authentication (see below)
- [x] VSCode extensions
- [x] Flask Codespace environment
- [x] Flask unit tests
- [x] Sphinx documentation with Google-style docstrings
- [x] Swagger documentation

## Authentication

This API template works with either basic or key-based authentication.  Behavior is based on the `FLASK_API_AUTH_TYPE` environment variable:
| Value | Authentication Mode |
|---|---|
| none | Basic Auth |
| `BASIC` | Basic Auth |
| `API_KEY` | API Key |

## Helpful Commands

Here's a quick overview of some helpful commands for managing this repository:

| Task | Command |
|---|---|
| Run API | `python3 flask_api/api.py` |
| Run unit tests | `python3 -m unittest discover` |
| Rebuild `requirements.txt` | `pip freeze > requirements.txt` |
| Rebuild Sphinx documentation | `make html` |
