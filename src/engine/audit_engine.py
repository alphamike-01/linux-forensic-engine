import json

audit_trail = []


def record(
    event,
    anomalies,
    state_changes
):

    audit_trail.append(

        {

            "event_id":
            event.event_id,

            "timestamp":
            event.timestamp,

            "source":
            event.source,

            "event_type":
            event.event_type,

            "anomalies":
            anomalies,

            "state_changes":
            state_changes
        }
    )


def get_audit_trail():

    return audit_trail
