from flask import Flask
from flask import jsonify
from flask import request

from src.models.event import Event
from src.models.state import State

from src.engine.state_engine import apply_event

from src.engine.audit_engine import (
    record,
    get_audit_trail
)


app = Flask(__name__)


@app.post("/events")
def replay():

    state = State()

    events = request.json

    for index, item in enumerate(events):

        event = Event(

            event_id=f"api_{index}",

            timestamp=item["timestamp"],

            source=item["source"],

            event_type=item["event_type"],

            details=item["details"]
        )

        state = apply_event(
            state,
            event
        )

        record(
            event,
            [],
            []
        )

    return jsonify(

        {

            "state":
            state.to_dict(),

            "audit_trail":
            get_audit_trail()
        }
    )


if __name__ == "__main__":
	app.run(
		host="127.0.0.1",
		port=5000,
		debug=True
	)
