import re

from src.models.event import Event

from src.parsers.time_utils import (
    normalize_timestamp
)


def parse_audit(filepath):

    events = []

    with open(filepath, "r") as file:

        for index, line in enumerate(file):

            line = line.strip()

            if not line:

                continue

            timestamp = re.search(
                r"audit\((.*?)\)",
                line
            ).group(1)

            pid = int(
                re.search(
                    r"pid=(\d+)",
                    line
                ).group(1)
            )

            ppid = int(
                re.search(
                    r"ppid=(\d+)",
                    line
                ).group(1)
            )

            uid = int(
                re.search(
                    r"uid=(\d+)",
                    line
                ).group(1)
            )

            exe = re.search(
                r"exe=(.*)",
                line
            ).group(1)

            events.append(

                Event(

                    event_id=f"audit_{index}",

                    timestamp=normalize_timestamp(
                        timestamp
                    ),

                    source="audit",

                    event_type="process_start",

                    details={

                        "pid": pid,

                        "ppid": ppid,

                        "uid": uid,

                        "exe": exe
                    }
                )
            )

    return events
