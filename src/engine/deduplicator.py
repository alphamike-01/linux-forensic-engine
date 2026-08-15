def remove_duplicates(events):

    seen = set()

    unique_events = []

    for event in events:

        key = (

            event.timestamp,

            event.source,

            event.event_type,

            str(event.details)
        )

        if key not in seen:

            seen.add(key)

            unique_events.append(event)

    return unique_events
