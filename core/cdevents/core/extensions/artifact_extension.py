"""ArtifactExtension represents the extension for extension context."""

from cloudevents.http import CloudEvent

ArtifactIdExtension = "artifactid"
ArtifactNameExtension = "artifactname"
ArtifactVersionExtension = "artifactversion"


class ArtifactExtension:
    """Artifact Extension."""

    def __init__(self) -> None:
        pass

    def read_transformer():
        """Read transformer."""
        pass

    def write_transformer(event: CloudEvent, extensions: dict) -> CloudEvent:
        """Write transformer."""
        if event._attributes["extensions"].get(ArtifactIdExtension):
            event._attributes["extensions"].set(
                ArtifactIdExtension, extensions.get(ArtifactIdExtension)
            )
        if event._attributes["extensions"].get(ArtifactNameExtension):
            event._attributes["extensions"].set(
                ArtifactNameExtension, extensions.get(ArtifactNameExtension)
            )
        if event._attributes["extensions"].get(ArtifactVersionExtension):
            event._attributes["extensions"].set(
                ArtifactVersionExtension, extensions.get(ArtifactVersionExtension)
            )
        return event
