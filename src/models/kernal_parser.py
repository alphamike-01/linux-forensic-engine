from src.models.event import Event


def parse_kernel(filepath):

    events = []

    with open(filepath) as file:

        for line in file:

            data = line.strip().split(",")

            events.append(
                Event(
                    timestamp=data[0],
                    source="kernel_module",
                    event_type=data[1],
                    details={
                        "pid": int(data[2]),
                        "path": data[3],
                        "action": data[4],
                        "uid": int(data[5])
                    }
                )
            )

    return events
