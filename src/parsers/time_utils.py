from datetime import datetime
from datetime import timezone


def normalize_timestamp(timestamp):

    if timestamp.endswith("Z"):

        timestamp = timestamp.replace(
            "Z",
            "+00:00"
        )

    dt = datetime.fromisoformat(
        timestamp
    )

    return dt.astimezone(
        timezone.utc
    ).isoformat()
