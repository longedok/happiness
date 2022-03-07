build:
	docker build -f docker/django/Dockerfile -t longedok/happiness:latest .

push:
	docker push longedok/happiness:latest

upload:
	DJANGO_ENV=production docker build -f docker/django/Dockerfile -t longedok/happiness:latest .
	docker push longedok/happiness:latest

update:
	docker-compose -f docker-compose.yml -f docker/docker-compose.prod.yml up -d --no-deps web

deploy:
	pass show test
	docker pull longedok/happiness:latest
	docker-compose -f docker-compose.yml -f docker/docker-compose.prod.yml up -d --no-deps web

deploy_full:
	pass show test
	docker pull longedok/happiness:latest
	docker-compose -f docker-compose.yml -f docker/docker-compose.prod.yml up -d

restart:
	docker-compose up -d --no-deps --force-recreate web

shell:
	docker-compose run --rm web ./manage.py shell

bash:
	docker-compose run --rm web bash

bash_prod:
	docker-compose -f docker-compose.yml -f docker/docker-compose.prod.yml run --rm web bash
