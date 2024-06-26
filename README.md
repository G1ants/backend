# Backend
The backend infrastructure for Giants

## Install Poetry

We use [Poetry](https://python-poetry.org/) for dependency management.

```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -
```

Or follow installation instructions from [Poetry website](https://python-poetry.org/docs/#installation).

## Setup Virtual Environment

It is recommended to use Python virtual environment, so you don't pollute your system Python environment.

```bash
# Install dependencies
poetry install
```

```bash
# Update/upgrade dependencies
poetry update
```

```bash
# Activate Python virtual environment
poetry shell
```

## Environment Variables
Copy an existing environment template file and fill in all the necessary values:
```bash
# Create .env file (by copying from .env.example)
cp .env.example .env
```

### Start the server

```
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

### Install turso CLI

https://docs.turso.tech/quickstart

### For windows users
You will need windows wsl to run the turso CLI. You can follow the instructions here: https://docs.microsoft.com/en-us/windows/wsl/install
Perform the turso installation in the wsl terminal.

### Login to turso
```
turso auth logout
turso auth login (make sure u are on the right browser with the right account)
turso org switch ****YOUR USERNAME****
turso db list (u should see the correct db)
```

### Check style

Run the following command at the root of the repository
`black .`
