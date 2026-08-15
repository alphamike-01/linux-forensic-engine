import re

from datetime import datetime

from src.models.event import Event


def parse_audit(filepath):

    events = []

    with open(filepath) as file:

        for line in file:

            if not line.strip():
                continue

            pid = int(re.search(r"pid=(\d+)", line).group(1))

            ppid = int(re.search(r"ppid=(\d+)", line).group(1))

            uid = int(re.search(r"uid=(\d+)", line).group(1))

            exe = re.search(r"exe=(.+)", line).group(1)

            timestamp = datetime.utcnow().isoformat()

            events.append(
                Event(
                    timestamp=timestamp,
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
