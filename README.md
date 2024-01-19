# sdk-python

Python SDK for CDEvents

The SDK can be used to create CDEvents in CloudEvents form, for use with the
  [CloudEvents Python SDK](https://github.com/cloudevents/sdk-python).

## Disclaimer 🚧

This SDK is work in work in progress, it will be maintained in sync with the
specification and it now covers all events from the specification.

## Get started

Clone the repo and install the Python SDK as a package:

```golang
cd src && pip install .
```

And import the module in your code

```golang
import cdevents
```

## Create your first CDEvent

To create a CDEvent, for instance a [*pipelineRun queued*](https://cdevents.dev/docs/core/#pipelinerun-queued) one:

```python
import cdevents

event = cdevents.new_pipelinerun_queued_event(
    context_id="my-context-id",
    context_source="my/first/cdevent/program",
    context_timestamp=datetime.datetime.now(),
    subject_id="myPipelineRun1",
    custom_data={"hello_message": "hi!"},
    subject_source="subjectSource",
    custom_data_content_type="application/json",
    pipeline_name="myPipeline",
    url="https://example.com/myPipeline",
)
```

## Send your first CDEvent as CloudEvent

To send a CDEvent as CloudEvent:

```python
import cdevents

# Create a CloudEvent from the CDEvent
cloudevent = cdevents.to_cloudevent(event)

# Creates the HTTP request representation of the CloudEvent in structured content mode
headers, body = to_structured(event)

# POST
requests.post("<some-url>", data=body, headers=headers)

```

See the [CloudEvents](https://github.com/cloudevents/sdk-python) docs as well.

## References

- [CDEvents](https://cdevents.dev)
- [CDFoundation SIG Events Vocabulary Draft](https://github.com/cdfoundation/sig-events/tree/main/vocabulary-draft)
