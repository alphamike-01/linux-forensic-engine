SOURCE_PRIORITY = {

    "kernel_module": 1,

    "audit": 2,

    "dmesg": 3
}


def reconcile(events):

    events.sort(

        key=lambda event: (

            event.timestamp,

            SOURCE_PRIORITY.get(
                event.source,
                999
            ),

            event.details.get(
                "pid",
                999999
            )
        )
    )

    return events
