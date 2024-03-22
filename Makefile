format:
	poetry run black .
	poetry run ruff . --fix 

test:
	poetry run pytest --cov=html_elements --cov-report term-missing tests/

lint:
	poetry run black . --check 
	poetry run ruff .
	poetry run pyright .
	poetry run mypy . --check-untyped-defs

check: test lint

docs-build:
	poetry run mkdocs build

docs-run:
	poetry run mkdocs serve
