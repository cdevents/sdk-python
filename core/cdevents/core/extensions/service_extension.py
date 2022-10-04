"""ServiceExtension represents the extension for extension context."""

from cloudevents.http import CloudEvent

ServiceEnvIdExtension = "serviceenvid"
ServiceNameExtension = "servicename"
ServiceVersionExtension = "serviceversion"


class ServiceExtension:
    """Service Extension."""

    def __init__(self) -> None:
        pass

    def read_transformer():
        """Read transformer."""
        pass

    def write_transformer(event: CloudEvent, extensions: dict) -> CloudEvent:
        """Write transformer."""
        if event._attributes["extensions"].get(ServiceEnvIdExtension):
            event._attributes["extensions"].set(
                ServiceEnvIdExtension, extensions.get(ServiceEnvIdExtension)
            )
        if event._attributes["extensions"].get(ServiceNameExtension):
            event._attributes["extensions"].set(
                ServiceNameExtension, extensions.get(ServiceNameExtension)
            )
        if event._attributes["extensions"].get(ServiceVersionExtension):
            event._attributes["extensions"].set(
                ServiceVersionExtension, extensions.get(ServiceVersionExtension)
            )
        return event
