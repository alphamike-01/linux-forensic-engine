from src.models.event import Event

from src.parsers.time_utils import (
    normalize_timestamp
)


def parse_kernel(filepath):

    events = []

    with open(filepath, "r") as file:

        for index, line in enumerate(file):

            line = line.strip()

            if not line:

                continue

            data = line.split(",")

            pid = -1

            if data[2]:

                pid = int(data[2])

            events.append(

                Event(

                    event_id=f"kernel_{index}",

                    timestamp=normalize_timestamp(
                        data[0]
                    ),

                    source="kernel_module",

                    event_type=data[1],

                    details={

                        "pid": pid,

                        "path": data[3],

                        "action": data[4],

                        "uid": int(data[5])
                    }
                )
            )

    return events
