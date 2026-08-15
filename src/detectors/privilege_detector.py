def detect_privilege_escalation(
    event
):

    if (
        event.event_type
        !=
        "process_start"
    ):

        return None

    uid = event.details.get(
        "uid"
    )

    if uid == 0:

        return {

            "type":
            "privilege_escalation",

            "message":
            "Root privilege obtained",

            "event":
            event.event_id
        }

    return None

