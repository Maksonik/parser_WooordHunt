lint:
	poetry run ruff check --fix && poetry run ruff format

test:
	poetry run pytest -vv

test-cov:
	poetry run pytest --cov tests/ --cov-report=xml  --vcr-record=none
