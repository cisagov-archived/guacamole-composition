<<<<<<< HEAD
#!/usr/bin/env pytest -vs
"""Tests for Docker composition."""
=======
"""Tests for example container."""
>>>>>>> 0d48ebd47a28a887868ea3093e675e95f3843561

# Standard Python Libraries
import time

<<<<<<< HEAD
READY_MESSAGES = {
    "guacamole": "Server startup in",
    "guacd": "Listening on host 0.0.0.0",
    "postgres": "database system is ready to accept connections",
}
=======
# Third-Party Libraries
import pytest

ENV_VAR = "ECHO_MESSAGE"
ENV_VAR_VAL = "Hello World from docker compose!"
READY_MESSAGE = "This is a debug message"
DIVISION_MESSAGE = "8 / 2 == 4.000000"
SECRET_QUOTE = "Three may keep a secret, if two of them are dead."  # nosec
RELEASE_TAG = os.getenv("RELEASE_TAG")
VERSION_FILE = "src/version.txt"
>>>>>>> 0d48ebd47a28a887868ea3093e675e95f3843561


def test_container_count(dockerc):
    """Verify the test composition and container."""
    # all parameter allows non-running containers in results
    assert (
        len(dockerc.compose.ps(all=True)) == 5
    ), "Wrong number of containers were started."


def test_wait_for_ready_guacamole(guacamole_container):
    """Wait for guacamole container to be ready."""
    TIMEOUT = 20
    ready_message = READY_MESSAGES["guacamole"]
    for i in range(TIMEOUT):
        if ready_message in guacamole_container.logs():
            break
        time.sleep(1)
    else:
        raise Exception(
            f"Container does not seem ready.  "
            f'Expected "{ready_message}" in the log within {TIMEOUT} seconds.'
        )


def test_wait_for_ready_guacd(guacd_container):
    """Wait for guacd container to be ready."""
    TIMEOUT = 10
    ready_message = READY_MESSAGES["guacd"]
    for i in range(TIMEOUT):
        if ready_message in guacd_container.logs():
            break
        time.sleep(1)
    else:
        raise Exception(
            f"Container does not seem ready.  "
            f'Expected "{ready_message}" in the log within {TIMEOUT} seconds.'
        )


<<<<<<< HEAD
def test_wait_for_ready_postgres(postgres_container):
    """Wait for postgres container to be ready."""
    TIMEOUT = 10
    ready_message = READY_MESSAGES["postgres"]
    for i in range(TIMEOUT):
        if ready_message in postgres_container.logs():
            break
        time.sleep(1)
    else:
        raise Exception(
            f"Container does not seem ready.  "
            f'Expected "{ready_message}" in the log within {TIMEOUT} seconds.'
        )
=======
def test_output(dockerc, main_container):
    """Verify the container had the correct output."""
    # make sure container exited if running test isolated
    dockerc.wait(main_container.id)
    log_output = main_container.logs()
    assert DIVISION_MESSAGE in log_output, "Division message not found in log output."
    assert SECRET_QUOTE in log_output, "Secret not found in log output."


@pytest.mark.skipif(
    RELEASE_TAG in [None, ""], reason="this is not a release (RELEASE_TAG not set)"
)
def test_release_version(project_version):
    """Verify that release tag version agrees with the module version."""
    assert (
        RELEASE_TAG == f"v{project_version}"
    ), "RELEASE_TAG does not match the project version"


def test_log_version(dockerc, project_version, version_container):
    """Verify the container outputs the correct version to the logs."""
    # make sure container exited if running test isolated
    dockerc.wait(version_container.id)
    log_output = version_container.logs().strip()
    assert (
        log_output == project_version
    ), f"Container version output to log does not match project version file {VERSION_FILE}"


@pytest.mark.skipif(
    RELEASE_TAG in [None, ""], reason="this is not a release (RELEASE_TAG not set)"
)
def test_container_version_label_matches(project_version, version_container):
    """Verify the container version label is the correct version."""
    assert (
        version_container.config.labels["org.opencontainers.image.version"]
        == project_version
    ), "Dockerfile version label does not match project version"
>>>>>>> 0d48ebd47a28a887868ea3093e675e95f3843561
