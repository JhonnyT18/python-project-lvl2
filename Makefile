lint:
	@poetry run flake8 gendiff


build:
	@poetry build


run_tests:
	@poetry run pytest --cov-report xml
