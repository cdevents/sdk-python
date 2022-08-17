from flask import Flask, request

from cdevents.core.http_handlar import HttpHandlar

app = Flask(__name__)


# create an endpoint at http://localhost:/8080/
@app.route("/", methods=["POST"])
def home():
    # create a CloudEvent
    event = HttpHandlar.event_from_http(headers=request.headers, data=request.get_data())

    # you can access cloudevent fields as seen below
    print(
        f"Found {event['id']} from {event['source']} with type "
        f"{event['type']} and specversion {event['specversion']}"
    )
    print()
    print(event)
    return "", 204


if __name__ == "__main__":
    app.run(port=8080)