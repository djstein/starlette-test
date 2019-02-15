# starlette test

Async webframework test with GraphQL

## Install

```
pyenv install 3.7.2
git clone git@github.com:djstein/starlette-test.git
cd startlette-test
virtualenv .venv
source .venv/bin/activate
pip install -Ur requirements/requirements.txt
pip install -Ur requirements/requirements-dev.txt
```

## Run the application

```
python app.py
```

navigate to 0.0.0.0:8000

## Available Endpoints

```
http://0.0.0.0:8000/
http://0.0.0.0:8000/graph/v1/
```

## Available GraphQL Queries

```
{
    hello()
}

{
    hello(name: "Reico")
}
```

Create initial migrations

```
alembic revision --autogenerate -m "initial"
```

Run migrations

```
alembic upgrade head
```
