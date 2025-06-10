run:
	python manage.py runserver

lint:
	ruff check . && ruff check . --diff

format:
	ruff check . --fix && ruff format .

test:
	PYTHONPATH=. pytest

seed:
	python manage.py shell < entries/seed_entries.py