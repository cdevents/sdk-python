import typing
import json

# from cloudevents.http import from_http
import cloudevents.exceptions as cloud_exceptions
from cloudevents.http.event import CloudEvent
from cloudevents.http.event_type import is_binary
from cloudevents.http.mappings import _obj_by_version
from cloudevents.http.util import _json_or_string
from cloudevents.sdk import marshaller, types


from cdevents.core.event import Event
from cdevents.core.event_type import EventType

from cdevents.core.artifact import ArtifactPackagedEvent, ArtifactPublishedEvent
from cdevents.core.build import BuildStartedEvent, BuildFinishedEvent, BuildQueuedEvent

class HttpHandlar():
    """Http Handlar."""

    def get_attrs(
            headers: typing.Dict[str, str],
            data: typing.Union[str, bytes, None],
            data_unmarshaller: types.UnmarshallerType = None,
        ):
            """
            Unwrap a CD_evnets (binary or structured) from an HTTP request.
            :param headers: the HTTP headers
            :type headers: typing.Dict[str, str]
            :param data: the HTTP request body. If set to None, "" or b'', the returned
                event's data field will be set to None
            :type data: typing.IO
            :param data_unmarshaller: Callable function to map data to a python object
                e.g. lambda x: x or lambda x: json.loads(x)
            :type data_unmarshaller: types.UnmarshallerType
            """
            if data is None or data == b"":
                # Empty string will cause data to be marshalled into None
                data = ""

            if not isinstance(data, (str, bytes, bytearray)):
                raise cloud_exceptions.InvalidStructuredJSON(
                    "Expected json of type (str, bytes, bytearray), "
                    f"but instead found type {type(data)}"
                )

            headers = {key.lower(): value for key, value in headers.items()}
            if data_unmarshaller is None:
                data_unmarshaller = _json_or_string

            marshall = marshaller.NewDefaultHTTPMarshaller()

            if is_binary(headers):
                specversion = headers.get("ce-specversion", None)
            else:
                try:
                    raw_ce = json.loads(data)
                except json.decoder.JSONDecodeError:
                    raise cloud_exceptions.MissingRequiredFields(
                        "Failed to read specversion from both headers and data. "
                        f"The following can not be parsed as json: {data}"
                    )
                if hasattr(raw_ce, "get"):
                    specversion = raw_ce.get("specversion", None)
                else:
                    raise cloud_exceptions.MissingRequiredFields(
                        "Failed to read specversion from both headers and data. "
                        f"The following deserialized data has no 'get' method: {raw_ce}"
                    )

            if specversion is None:
                raise cloud_exceptions.MissingRequiredFields(
                    "Failed to find specversion in HTTP request"
                )

            event_handler = _obj_by_version.get(specversion, None)

            if event_handler is None:
                raise cloud_exceptions.InvalidRequiredFields(
                    f"Found invalid specversion {specversion}"
                )

            event = marshall.FromRequest(
                event_handler(), headers, data, data_unmarshaller=data_unmarshaller
            )
            # if event.data == "" or event.data == b"":
            #     # TODO: Check binary unmarshallers to debug why setting data to ""
            #     # returns an event with data set to None, but structured will return ""
            #     data = None
            attrs = event.Properties()
            return attrs


    def event_from_http(headers: typing.Dict[str, str],
            data: typing.Union[str, bytes, None],
            data_unmarshaller: types.UnmarshallerType = None
            ):
        attrs = HttpHandlar.get_attrs(headers, data, data_unmarshaller)

        event_data=attrs.pop("data", None)
        extensions=attrs.pop("extensions", None)

        etype = EventType(attrs.get("type"))
        if etype.value == "" or etype.value is None:
            raise cloud_exceptions.MissingRequiredFields(
                "Failed to find type in HTTP request"
            )
        elif etype.value == EventType.ArtifactPackagedEventV1.value:
            return ArtifactPackagedEvent(attrs=attrs, extensions=extensions, data=event_data)
        elif etype.value == EventType.ArtifactPublishedEventV1.value:
            return ArtifactPublishedEvent(attrs=attrs, extensions=extensions, data=event_data)
        elif etype.value == EventType.BuildStartedEventV1.value:
            return BuildStartedEvent(attrs=attrs, extensions=extensions, data=event_data)
        elif etype.value == EventType.BuildQueuedEventV1.value:
            return BuildQueuedEvent(attrs=attrs, extensions=extensions, data=event_data)
        elif etype.value == EventType.BuildFinishedEventV1.value:
            return BuildFinishedEvent(attrs=attrs, extensions=extensions, data=event_data)

        # e = BuildStartedEvent.create_from_event(event)
        # return e