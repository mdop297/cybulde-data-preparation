# Before running this project
- install git docker, docker compose, gcloud
- add ssh key from local machine to github
- run `gcloud init` or [gcloud auth application-default login](https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login)

# create pyproject.toml and add dependencies

- dependencies install for project under [tool.poetry.dependencies]  
- dependencies install for development state: [tool.poetry.group.dev.dependencies]
- optional dependencies: [tool.poetry.group.docs.dependencies]

# create Dockerfile, .dokerignore, docker compose

- In this project we mount current directory to container. So that, we need to have permission to modify data in container by creating a new user in docker container, if not the container will be own by the root user in container and we can not modify it. 

- The PATH variable in the second ENV layer: add those three bin directories to the PATH variable
- pyproject.toml and poetry.lock flow: 
    - copied from current directory (the *.lock file can exists or not, we will handle both cases)
    - install the dependencies in docker container by using poetry.lock (first priority) or pyproject.toml
    - copy the generated (or the copied) .lock file to BUILD_POETRY_LOCK location

# Create Makefile
- The make commands:
    - make build: build docker image with the same poetry.lock file in current dir.
    - make build-for-dependencies: we want to build a NEW DOCKER IMAGE with the new dependencies.
    - make lock-dependencies: copy the generated content from the NEW DOCKER IMAGE to repo directory.

# Create configs, config schemas and utils
- We import file from configs and utils, so in those 2 folders we have __init__.py while config_schemas doesn't

# Questions
- Why do we ignore the docker-compose.yaml in .dockerignore? 
- Why do we custom @hydra.main decorator in get_config? >> OK
- How does get_config decorator in utils.config_utils.py work?
- Why do we create a new user in Dockerfile? >> OK
