build:
	docker build -f docker/django/Dockerfile -t longedok/happiness:0.1.5 .

push:
	docker push longedok/happiness:0.1.5

update:
	docker-compose -f docker-compose.yml -f docker/docker-compose.prod.yml up -d --no-deps web

deploy:
	pass show test
	docker pull longedok/happiness:0.1.5
	docker-compose -f docker-compose.yml -f docker/docker-compose.prod.yml up -d --no-deps web
