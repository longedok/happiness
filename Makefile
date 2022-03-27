prod_compose = -f docker-compose.yml -f docker/docker-compose.prod.yml

up:
	docker-compose up -d

down:
	docker-compose stop

web_log:
	docker-compose logs --tail=20 -f web

caddy_log:
	docker-compose $(prod_compose) logs --tail=20 -f caddy

build:
	docker build -f docker/django/Dockerfile -t longedok/happiness:latest .

push:
	docker push longedok/happiness:latest

upload:
	DJANGO_ENV=production docker build -f docker/django/Dockerfile -t longedok/happiness:latest .
	docker push longedok/happiness:latest

start_web:
	pass show test
	docker-compose $(prod_compose) up -d --no-deps web

stop_web:
	pass show test
	docker-compose $(prod_compose) stop web

deploy:
	pass show test
	docker pull longedok/happiness:latest
	docker-compose $(prod_compose) up -d --no-deps web

deploy_full:
	pass show test
	docker pull longedok/happiness:latest
	docker-compose $(prod_compose) up -d

deploy_full_force:
	pass show test
	docker pull longedok/happiness:latest
	docker-compose $(prod_compose) up -d --force-recreate

startup:
	docker-compose $(prod_compose) up -d

shutdown:
	docker-compose $(prod_compose) stop

restart_web:
	docker-compose up -d --no-deps --force-recreate web

shell:
	docker-compose run --rm web ./manage.py shell

bash:
	docker-compose run --rm web bash

bash_prod:
	docker-compose $(prod_compose) run --rm web bash

psql:
	docker-compose run --rm db psql -h db -p 5432 -d happiness -U happiness

psql_prod:
	docker-compose $(prod_compose) run --rm db psql -h db -d happiness -U happiness

pass:
	pass show test
