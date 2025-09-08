lint:
	ruff check . && ruff check . --diff

format:
	ruff check . --fix && ruff format .

run:
	python manage.py runserver