install:
	@poetry install


lint:
	@poetry run flake8 gendiff


build:
	@poetry build


test:
	poetry run pytest --cov=gendiff --cov-report xml tests/


coverage:
	@poetry run coverage xml

.PHONY: install lint build test test-cov coverage