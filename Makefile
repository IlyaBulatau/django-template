build:
	docker compose --env-file ./env/.env.dev -f docker-compose.dev.yaml build

run:
	docker compose --env-file ./env/.env.dev -f docker-compose.dev.yaml up -d

restart:
	docker restart $$(docker ps -a -q)

migrations:
	docker exec app poetry run python3 ./src/manage.py makemigrations

migrate:
	docker exec app poetry run python3 ./src/manage.py migrate

stop:
	docker stop $$(docker ps -a -q)

delete:
	docker delete $$(docker ps -a -q)

rebuld:
	make build
	make run

logs:
	docker logs app -f