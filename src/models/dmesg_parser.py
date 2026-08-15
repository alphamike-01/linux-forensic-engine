from datetime import datetime

from src.models.event import Event


def parse_dmesg(filepath):

    events = []

    with open(filepath) as file:

        for line in file:

            if not line.strip():
                continue

            events.append(
                Event(
                    timestamp=datetime.utcnow().isoformat(),
                    source="dmesg",
                    event_type="kernel_message",
                    details={
                        "message": line.strip()
                    }
                )
            )

    return events
