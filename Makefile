.PHONY: activate
activate: ## activate the virtualenv associate with this project
	pipenv shell

# @see http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.DEFAULT_GOAL := help
.PHONY: help
help: ## provides cli help for this makefile (default)
	@grep -E '^[a-zA-Z_0-9-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: ## remove all transient directories and files
	rm -rf dist
	rm -f .coverage
	rm -rf *.egg-info
	rm -f MANIFEST
	find -name __pycache__ -print0 | xargs -0 rm -rf
	pipenv --rm

.PHONY: freeze_requirements
freeze_requirements: ## update the project dependencies based on setup.py declaration
	pipenv update

.PHONY: install_requirements_dev
install_requirements_dev: ## install pip requirements for development
	pipenv install --dev

.PHONY: install_requirements
install_requirements: ## install pip requirements based on requirements.txt
	pipenv install

.PHONY: up
up: ## run the database and execute dbli upgrade command
	docker-compose up
