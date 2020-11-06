install:
	@poetry install


lint:
	@poetry run flake8 gendiff


build:
	@poetry build


test:
	@poetry run pytest --cov-report xml
