# Goodreads Project

## Prerequisite

- Support of `Make` file to run instruction commands.

## Run Project

```shell
cd to/projct/directory

# Create docker network.
docker network create goodreads_network

# Create env files using their templates.
make copy_env_files

# Adjust env variables with appropriate values - using an editor like vim.
vim ./envs/app.env
vim ./envs/db.env
vim ./.env

# To build and up docker images:
make run
# or in case for detached mode, run following:
make run_detach

# For more information and examples:
make help
```

## Run Unit-Tests

```shell
make tests_all v=2
```

## Naming Conventions & Definitions

```text
SRL: Serializer > *_srl.py
VLD: Validator > class AppsRepoCreateVLD(...
TRF: Transformer > class UsersViewSignUpTRF(...
Repo: Repository > *_repo.py , class AppsRepo:...
SVC: Service > *_svc.py
```

- A Serializer can play the roles of a Validator or Transformer.
- A Transformer is used for transforming given instance(s) to another schema.
- A Validator is used for validating given data according to its fields.
- A Service is used for maintaining the main logic of app.
- A Repository is an ORM logic layer used for working with models.

## More Information

```shell
make help
```

## Documents

- [Github Repository](https://github.com/ykh/goodreads)
- [Project Management Board - Trello](https://trello.com/b/JdvUrNzB/goodreads-bb)
- [API Doc - Postman](https://www.postman.com/develozerg/workspace/goodreads-bb/overview)
