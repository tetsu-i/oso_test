## setup
python3.10


### poetry install(if poetry is not installed)
`$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`

### app
1. `$ poetry install`
2. `$ docker-compose up -d`
3. `$ poetry run alembic upgrade head`
4. `$ poetry run python -m myapp.fixture`

## test
`$ poetry run pytest tests -vv`