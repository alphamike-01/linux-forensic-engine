import re

from src.models.event import Event

from src.parsers.time_utils import (
    normalize_timestamp
)


def parse_dmesg(filepath):

    events = []

    with open(filepath, "r") as file:

        for index, line in enumerate(file):

            line = line.strip()

            if not line:

                continue

            timestamp = re.search(
                r"\[(.*?)\]",
                line
            ).group(1)

            message = re.sub(
                r"\[.*?\]",
                "",
                line
            ).strip()

            events.append(

                Event(

                    event_id=f"dmesg_{index}",

                    timestamp=normalize_timestamp(
                        timestamp
                    ),

                    source="dmesg",

                    event_type="kernel_message",

                    details={

                        "message": message
                    }
                )
            )

    return events
