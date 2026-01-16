.PHONY: run makemigrations migrate createsuperuser shell
run:
	python3 manage.py runserver
makemigrations:
	python3 manage.py makemigrations
migrate:
	python3 manage.py migrate
createsuperuser:
	python3 manage.py createsuperuser
shell:
	python3 manage.py shell