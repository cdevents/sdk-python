"""Constants for cdevents cli."""
from pathlib import Path

# configuration/configuration.yaml
_CLI_CDEVENTS_DIR = Path(__file__).parent.parent
DEAFULT_CONFIGURATION_FILE = str(Path(_CLI_CDEVENTS_DIR, "configuration", "configuration.yaml"))
LOGGING_CONFIGURATION_FILE = str(
    Path(_CLI_CDEVENTS_DIR, "configuration", "logging-configuration.yaml")
)

BYTES_IN_KILOBYTES = 1024
BYTES_IN_MEGABYTES = BYTES_IN_KILOBYTES * BYTES_IN_KILOBYTES
BYTES_IN_GIGABYTES = BYTES_IN_MEGABYTES * BYTES_IN_KILOBYTES
