clean:
	rm -rf .venv

dev:
	uv sync --all-groups
	uv pip install -e .

test:
	
	$(MAKE) start-test-db
	$(MAKE) dev
	export ENVIRONMENT=test && uv run pytest -s -n 4; \
	EXIT_CODE=$$?; \
	$(MAKE) stop-test-db; \
	exit $$EXIT_CODE

start-test-db:
	docker compose -f .docker/test-db-docker-compose.yml up -d

stop-test-db:
	docker compose -f .docker/test-db-docker-compose.yml down