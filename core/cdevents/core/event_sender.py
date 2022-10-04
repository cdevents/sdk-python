"""Core events sender."""

import requests
from cloudevents.http import CloudEvent, to_structured


class EventSender:
    """Events Sender."""

    def __init__(self, cde_link: str = ""):
        """Initializes class."""
        if cde_link:
            self._cde_link = cde_link
        else:
            self._cde_link = "http://localhost:8080"

    def send(self, event: CloudEvent):
        """Send the given event."""
        headers, body = to_structured(event)

        # send and print event
        result = requests.post(self._cde_link, headers=headers, data=body)
        print(f"Response with state code {result.status_code}")
