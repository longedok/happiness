build:
	docker build -f docker/django/Dockerfile -t longedok/happiness:latest .

push:
	docker push longedok/happiness:latest

upload:
	docker build -f docker/django/Dockerfile -t longedok/happiness:latest .
	docker push longedok/happiness:latest

update:
	docker-compose -f docker-compose.yml -f docker/docker-compose.prod.yml up -d --no-deps web

deploy:
	pass show test
	docker pull longedok/happiness:latest
	docker-compose -f docker-compose.yml -f docker/docker-compose.prod.yml up -d --no-deps web
