## setup
python3.10


### poetry install(if poetry is not installed)
`$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`

### app
`$ poetry install`
`$ docker-compose up -d`
`$ poetry run alembic upgrade head`
`$ poetry run python -m myapp.fixture`

## test
`$ poetry run pytest tests -vv`