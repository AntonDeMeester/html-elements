format:
	black .
	ruff . --fix

test:
	pytest --cov=html_elements --cov-report term-missing tests/

lint:
	black . --check
	ruff .
	pyright .
	mypy . --check-untyped-defs