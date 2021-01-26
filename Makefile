lint:
	flake8 .
	pylint manage.py surveys/

format:
	isort **/*.py
	black .
