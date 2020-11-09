install:
	@poetry install


lint:
	@poetry run flake8 gendiff


build:
	@poetry build


test:
	@poetry run pytest -v


test-cov:
	@poetry run coverage run --source=gendiff -m pytest
	@poetry run coverage xml


coverage:
	poetry run coverage xml

.PHONY: install lint build test test-cov coverage