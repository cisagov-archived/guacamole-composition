# guacamole-composition 🥑🐳 #

[![GitHub Build Status](https://github.com/cisagov/guacamole-composition/workflows/build/badge.svg)](https://github.com/cisagov/guacamole-composition/actions)
[![CodeQL](https://github.com/cisagov/guacamole-composition/workflows/CodeQL/badge.svg)](https://github.com/cisagov/guacamole-composition/actions/workflows/codeql-analysis.yml)
[![Known Vulnerabilities](https://snyk.io/test/github/cisagov/guacamole-composition/badge.svg)](https://snyk.io/test/github/cisagov/guacamole-composition)

Creates a Docker composition containing instances of:

- [guacamole](https://hub.docker.com/r/guacamole/guacamole/) clientless
remote desktop gateway.
- [guacd](https://hub.docker.com/r/guacamole/guacd/) server-side proxy for
Guacamole.
- [Postgres](https://hub.docker.com/_/postgres/) relational database.
- [cisagov/guacscanner-docker](https://github.com/cisagov/guacscanner-docker)
  utility for continually scanning the EC2 instances in an AWS VPC and
  updating the Guacamole connections in the underlying PostgreSQL
  database.

## Running ##

A sample [Docker composition](docker-compose.yml) is included
in this repository.

To start the composition, use the command: `docker compose up`

<<<<<<< HEAD
Connect to the Guacamole web interface at:
[http://localhost/guacamole](http://localhost/guacamole).
=======
```console
docker run cisagov/example:0.2.0
```
>>>>>>> 0d48ebd47a28a887868ea3093e675e95f3843561

The default credentials are `guacadmin`, `guacadmin` - you should change those
as soon as possible.

### Volumes ###

#### postgres ####

<<<<<<< HEAD
| Mount Point | Purpose |
| ----------- | ------- |
| `dbdata` | Stores all database data for the `postgres` container |
| `dbinit` | Stores the `postgres` initialization script for the `guacamole` database resources |
=======
    services:
      example:
        image: cisagov/example:0.2.0
        volumes:
          - type: bind
            source: <your_log_dir>
            target: /var/log
        environment:
          - ECHO_MESSAGE="Hello from docker compose"
        ports:
          - target: 8080
            published: 8080
            protocol: tcp
    ```
>>>>>>> 0d48ebd47a28a887868ea3093e675e95f3843561

### Ports ###

This composition exposes the following port to the `localhost`:

| Port  | Protocol | Service  | Purpose |
|-------|----------|----------|---------|
| 80    | TCP      | http     | Guacamole web interface |

### Secrets ###

Sample secrets have been provided - you should change these if you use this
composition on a publicly-accessible host:

<<<<<<< HEAD
| Filename | Purpose |
|----------|---------|
| postgres_username | Text file containing the username of the `postgres` user used by the `guacamole` container |
| postgres_password | Text file containing the password of the `postgres` user used by the `guacamole` container |
| private_ssh_key | Text file containing the private SSH key to use for SFTP file transfer in Guacamole. |
| rdp_username | Text file containing the username for Guacamole to use when connecting to an instance via RDP. |
| rdp_password | Text file containing the password for Guacamole to use when connecting to an instance via RDP. |
| vnc_username | Text file containing the username for Guacamole to use when connecting to an instance via VNC. |
| vnc_password | Text file containing the password for Guacamole to use when connecting to an instance via VNC. |
| windows_sftp_base | Text file containing the base path for the SFTP directories that Guacamole will use when connecting to a Windows instance via VNC. |
=======
    ```text
    Better lock it in your pocket.
    ```

1. Then add the secret to your `docker-compose.yml` file:

    ```yaml
    ---
    version: "3.7"

    secrets:
      quote_txt:
        file: quote.txt

    services:
      example:
        image: cisagov/example:0.2.0
        volumes:
          - type: bind
            source: <your_log_dir>
            target: /var/log
        environment:
          - ECHO_MESSAGE="Hello from docker compose"
        ports:
          - target: 8080
            published: 8080
            protocol: tcp
        secrets:
          - source: quote_txt
            target: quote.txt
    ```

## Updating your container ##

### Docker Compose ###

1. Pull the new image from Docker Hub:

    ```console
    docker compose pull
    ```

1. Recreate the running container by following the [previous instructions](#running-with-docker-compose):

    ```console
    docker compose up --detach
    ```

### Docker ###

1. Stop the running container:

    ```console
    docker stop <container_id>
    ```

1. Pull the new image:

    ```console
    docker pull cisagov/example:0.2.0
    ```

1. Recreate and run the container by following the [previous instructions](#running-with-docker).

## Updating Python dependencies ##

This image uses [Pipenv] to manage Python dependencies using a [Pipfile](https://github.com/pypa/pipfile).
Both updating dependencies and changing the [Pipenv] configuration in `src/Pipfile`
will result in a modified `src/Pipfile.lock` file that should be committed to the
repository.

> [!WARNING]
> The `src/Pipfile.lock` as generated will fail `pre-commit` checks due to JSON formatting.

### Updating dependencies ###

If you want to update existing dependencies you would run the following command
in the `src/` subdirectory:

```console
pipenv lock
```

### Modifying dependencies ###

If you want to add or remove dependencies you would update the `src/Pipfile` file
and then update dependencies as you would above.

> [!NOTE]
> You should only specify packages that are explicitly needed for your Docker
> configuration. Allow [Pipenv] to manage the dependencies of the specified
> packages.

## Image tags ##

The images of this container are tagged with [semantic
versions](https://semver.org) of the underlying example project that they
containerize.  It is recommended that most users use a version tag (e.g.
`:0.2.0`).

| Image:tag | Description |
|-----------|-------------|
|`cisagov/example:0.2.0`| An exact release version. |
|`cisagov/example:0.2`| The most recent release matching the major and minor version numbers. |
|`cisagov/example:0`| The most recent release matching the major version number. |
|`cisagov/example:edge` | The most recent image built from a merge into the `develop` branch of this repository. |
|`cisagov/example:nightly` | A nightly build of the `develop` branch of this repository. |
|`cisagov/example:latest`| The most recent release image pushed to a container registry.  Pulling an image using the `:latest` tag [should be avoided.](https://vsupalov.com/docker-latest-tag/) |

See the [tags tab](https://hub.docker.com/r/cisagov/example/tags) on Docker
Hub for a list of all the supported tags.

## Volumes ##

| Mount point | Purpose        |
|-------------|----------------|
| `/var/log`  |  Log storage   |

## Ports ##

The following ports are exposed by this container:

| Port | Purpose        |
|------|----------------|
| 8080 | Example only; nothing is actually listening on the port |

The sample [Docker composition](docker-compose.yml) publishes the
exposed port at 8080.

## Environment variables ##

### Required ###

There are no required environment variables.

<!--
| Name  | Purpose | Default |
|-------|---------|---------|
| `REQUIRED_VARIABLE` | Describe its purpose. | `null` |
-->

### Optional ###

| Name  | Purpose | Default |
|-------|---------|---------|
| `ECHO_MESSAGE` | Sets the message echoed by this container.  | `Hello World from Dockerfile` |

## Secrets ##

| Filename     | Purpose |
|--------------|---------|
| `quote.txt` | Replaces the secret stored in the example library's package data. |

## Building from source ##

Build the image locally using this git repository as the [build context](https://docs.docker.com/engine/reference/commandline/build/#git-repositories):

```console
docker build \
  --tag cisagov/example:0.2.0 \
  https://github.com/cisagov/example.git#develop
```

## Cross-platform builds ##

To create images that are compatible with other platforms, you can use the
[`buildx`](https://docs.docker.com/buildx/working-with-buildx/) feature of
Docker:

1. Copy the project to your machine using the `Code` button above
   or the command line:

    ```console
    git clone https://github.com/cisagov/example.git
    cd example
    ```

1. Create the `Dockerfile-x` file with `buildx` platform support:

    ```console
    ./buildx-dockerfile.sh
    ```

1. Build the image using `buildx`:

    ```console
    docker buildx build \
      --file Dockerfile-x \
      --platform linux/amd64 \
      --output type=docker \
      --tag cisagov/example:0.2.0 .
    ```

## New repositories from a skeleton ##

Please see our [Project Setup guide](https://github.com/cisagov/development-guide/tree/develop/project_setup)
for step-by-step instructions on how to start a new repository from
a skeleton. This will save you time and effort when configuring a
new repository!
>>>>>>> 0d48ebd47a28a887868ea3093e675e95f3843561

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

[Pipenv]: https://pypi.org/project/pipenv/
