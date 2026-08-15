SOURCE_PRIORITY = {

    "kernel_module": 3,

    "audit": 2,

    "dmesg": 1
}


def resolve_conflict(

    old_event,

    new_event
):

    if (

        SOURCE_PRIORITY[
            new_event.source
        ]

        >

        SOURCE_PRIORITY[
            old_event.source
        ]
    ):

        return new_event

    if (

        new_event.timestamp

        >

        old_event.timestamp
    ):

        return new_event

    old_pid = old_event.details.get(
        "pid",
        999999
    )

    new_pid = new_event.details.get(
        "pid",
        999999
    )

    if new_pid < old_pid:

        return new_event

    return old_event
