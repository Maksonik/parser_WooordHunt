lint:
	poetry run ruff check --fix && poetry run ruff format

test:
	poetry run pytest -vv

test-cov:
	echo "ssssssssss"
