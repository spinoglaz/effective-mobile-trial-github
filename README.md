How to run
==========

Install python 3.12:

```
pyenv install 3.12
pyenv local 3.12
```

Install dependencies:

`pip install -r requirements.txt`

Setup github credentials via environment variables or modify `.env` file:
- GITHUB_TOKEN
- GITHUB_USER
- GITHUB_REPO

Run tests:

`pytest`
