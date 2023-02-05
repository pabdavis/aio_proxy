PROJECT_NAME=aio_proxy_app
TIME=60

# colors
GREEN = $(shell tput -Txterm setaf 2)
YELLOW = $(shell tput -Txterm setaf 3)
WHITE = $(shell tput -Txterm setaf 7)
RESET = $(shell tput -Txterm sgr0)
GRAY = $(shell tput -Txterm setaf 6)
TARGET_MAX_CHAR_NUM = 20

# Common

all: run

## Runs application. Builds, creates, starts, and attaches to containers for a service. | Common
run:
	@docker-compose up $(PROJECT_NAME)_app

## Rebuild test_aio_app_app container
build:
	@docker-compose build $(PROJECT_NAME)_app

## Stops application. Stops running container without removing them.
stop:
	@docker-compose stop

## Removes stopped service containers.
clean:
	@docker-compose down

## Runs command `bash` commands in docker container.
bash:
	@docker exec -it $(PROJECT_NAME) bash

## Formats code with `flake8`.
lint:
	@docker-compose run --rm $(PROJECT_NAME)_app flake8 $(PROJECT_NAME)

## Runs tests. | Tests
# test: lint
#	@docker-compose up test
#	@docker-compose stop test


## Runs application with development config.
adev: wait_resources
	adev runserver ./$(PROJECT_NAME)/__main__.py -p 8080

## Runs application with specified postgres and redis.
wait_resources:
	python3 -m $(PROJECT_NAME).utils.wait_script