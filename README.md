# Frontend

## About

This repository contains files of E-catalog frontend application. Two main parts of the app - the user web interface and the API client which connects to the backend app and DB. You can get or push data from/to the database with simple CRUD operations of the API. They are similar for two basic instanses - Places and Individuals:

```
# get all places
GET http://{backend_address}:5000/api/v1/places/

# get a particular place
GET http://{backend_address}:5000/api/v1/places/<uid>

# create a place
POST http://{backend_address}:5000/api/v1/places/

# update a particular place
PUT http://{backend_address}:5000/api/v1/places/<uid>

# delete a particular place
DELETE http://{backend_address}:5000/api/v1/places/<uid>

# get all individuals
GET http://{backend_address}:5000/api/v1/individuals

# get a particular individual
GET http://{backend_address}:5000/api/v1/individuals/<uid>

# create an individual
POST http://{backend_address}:5000/api/v1/individuals/

# update a particular individual
PUT http://{backend_address}:5000/api/v1/individuals/<uid>

# delete a particular individual
DELETE http://{backend_address}:5000/api/v1/individuals/<uid>
```

## Contributing

Since this is a young Python project, we assume that you already have Python >=3.6 in your system. Clone this repository to your machine and follow the instructions.

### Install requirements

First of all, we're using Poetry to manage dependencies (and to make our lives easier too).

Install Poetry (globally):

```bash, PowerShell, CMD
    pip install poetry
```

Than you should create a virtual environment (.venv) in the root directory of your project

```bash, PowerShell, CMD
    poetry config virtualenvs.in-project true
```

This repository already has *poetry.lock* and *pyproject.toml* files, so you simply install all dependencies by a single command:

```bash, PowerShell, CMD
    poetry install
```

:exclamation: Note that Poetry will install all dependencies in the project virtual environment. It means you won't be able to use them outside it.
To run any file or package inside the Poetry environment use `poetry run <name_of_file_or_package>`

### Run app

To run the project in the terminal use

```bash, PowerShell, CMD
    poetry run python -m backend
```

Or you can use 'Run and Debug' if you're using VS Code - the necessary *launch.json* file are already there. Use 'frontend' to run the app.

:exclamation: Note that this app is tightly connected to the backend app and to the database. You can start it without this connection, but it will be an app with only one start page. To see and use the hole functionality you need to start backend and database containers first (see [backend repository README](https://github.com/E-catalog/backend/blob/main/README.md))

### Docker

We use Docker containers to store different services of our project.
Docker Compose manages all of these stuff for us.
Therefore we advise to install Docker Desktop on your machine (use [link](https://www.docker.com/products/docker-desktop)).

This repository already has the *docker-compose.yml* file with instructions for Docker Compose. All you need is to create an *.env* file in the root directory and set environmental variables. Use *.env.default* as a template for this.

:exclamation: *.env* file will contain your personal data (keys, passwords, tokens, etc). Don't forget to add it in the *.gitignore* - do not share this info with the hole world.

To run the entire app with the Docker Compose use

```bash, PowerShell, CMD
    docker compose up -d
```

Alternatively, you may use `docker-compose up` and run the app using docker-compose binary. The `-d` or `--detach` flag is used to run containers in the background, so your terminal stays free for other actions.

To run a specific container

```bash, PowerShell, CMD
    docker compose run -d <container_name>
```

To stop the entire app use

```bash, PowerShell, CMD
    docker-compose stop -t1
```

Or type the name of the container to stop only this container. The `-t1` flag sets the stopping time to 1 sec. By default this value is 10 sec.

To shut down the entire app use

```bash, PowerShell, CMD
    docker compose down
```

### Using linters

We use **wemake-python-styleguide** - "the strictest and most opinionated Python linter ever". Actually it's just a **flake8** plugin with some other useful plugins. Poetry files already have all dependencies, so you'll have the hole package of the linter after runnig `poetry install`.

To check the hole app code run

```bash, PowerShell, CMD
    poetry run flake8 backend
    poetry run mypy backend
```

It will examine all python files in *backend* directory.
If you want to check any particular python file simply use `poetry run flake8 <path/file_name>` or the same for **mypy**.
