.PHONY: up

up: ## Start the application
	docker-compose -f ./ops/docker-compose.yml up -d
	@echo "Access UI: http://localhost:4321"

.PHONY: restart

restart: ## Restart the application
	docker-compose -f ./ops/docker-compose.yml restart
	@echo "Access UI: http://localhost:4321"

.PHONY: down

down: ## Stop the application
	docker-compose -f ./ops/docker-compose.yml down

.PHONY: kill

kill: ## Stop the application
	docker-compose -f ./ops/docker-compose.yml kill

.PHONY: build

build: ## Build the application
	docker-compose -f ./ops/docker-compose.yml build

.PHONY: exec front

exec: ## Execute a shell in the front service
	docker-compose -f ./ops/docker-compose.yml exec front sh

.PHONY: help
help:
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'