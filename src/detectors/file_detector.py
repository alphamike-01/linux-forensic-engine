CRITICAL_FILES = {

    "/etc/passwd",

    "/etc/shadow",

    "/etc/group"
}


def detect_file_tampering(
    event
):

    if (
        event.event_type
        !=
        "file_access"
    ):

        return None

    path = event.details.get(
        "path"
    )

    action = event.details.get(
        "action"
    )

    if (

        path in CRITICAL_FILES

        and

        action == "write"
    ):

        return {

            "type":
            "file_tampering",

            "message":
            f"{path} modified",

            "event":
            event.event_id
        }

    return None
