.PHONY: dev-db
dev-db:
	docker compose -f .docker/db-docker-compose.yml up