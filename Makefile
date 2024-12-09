.PHONY: dev-db
dev-db:
	docker compose --env-file .env -f .docker/db-docker-compose.yml up