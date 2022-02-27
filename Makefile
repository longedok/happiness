build:
	docker build -f docker/django/Dockerfile -t longedok/happiness:0.1.4 .

update:
	docker-compose -f docker-compose.yml -f docker/docker-compose.prod.yml up -d --no-deps web
