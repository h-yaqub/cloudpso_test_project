# CloudPSO Test Django Project

The platform is a web app for the company´s own internal users.

Internal users enter using credentials and have different levels of hierarchy to get access to the data.

This app works for following roles that you can add in `Role` model:

  - Admin (Superuser)
  - Manager (Manager module)
  - Admin Op (Inventory module)
  - HR (Employees module)

## Technology Stack

  - Python v3.9.0
  - Django v3.0
  - PostgreSQL
  - HTML
  - CSS
  - Bootstrap
  - Docker

## Run App

Run the app by following command with `Docker`.

    ./docker/scripts/run-app.sh

The app should be running and accessible at http://127.0.0.1:8000


## Development Steup

Create virtual environment.

    python3 -m venv venv

Activate virtual environment. You need to activate virtual environment before running any Django command. For example, any command starting with manage.py is a Django command.

    source venv/bin/activate

Install dependencies in virtual environment. You will have to run this command whenever you pull new changes from the server.

    pip install -r requirements-dev.txt

Create an environment file (.env) in the root of the project. You can get the initial file by copying env.sample to .env.

Run the migrations. You will have to run this command whenever you pull new changes from the server.

    ./manage.py migrate

Run the backend.

    ./manage.py runserver


## Docker Development Setup (Optional)

You can alternately use [Docker](https://www.docker.com/) to set up your development environment. Docker has the advantage of creating isolated development environments. To run Docker setup, do:

    ./docker/scripts/setup.sh

The above command will build the image, create .env file if it doesn't exist, and run the necessary one-time commands to configure the development environment.

### Create Dev superuser

Create a Dev superuser for initial login to the application

    ./docker/scripts/ssh.sh ./manage.py createsuperuser
and provide the info required.

Start the application container

    docker compose run --service-ports --name app --rm app bash

And from within the conatiner, run the backend by doing:

    ./manage.py runserver 0.0.0.0:8000

Open the browser and access the app at http://127.0.0.1:8000.

SSH into the app container by doing:

    docker exec -it app bash

This will allow you to run any Linux command in the container.


## Setup pre-commit

This project uses [pre-commit](https://pre-commit.com/) to ensure that code standard checks pass locally before pushing to the remote project repo. [Follow](https://pre-commit.com/#installation) the installation instructions, then set up hooks with `pre-commit install`.

Make sure everything is working correctly by running

    pre-commit run --all
