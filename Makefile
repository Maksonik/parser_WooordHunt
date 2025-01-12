lint:
	poetry run ruff check --fix && poetry run ruff format

test:
	poetry run pytest -vv

test-cov:
	poetry run pytest --cov=parser tests/ --cov-report=xml
