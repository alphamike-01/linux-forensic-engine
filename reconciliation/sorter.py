def order(events):

    return sorted(
        events,
        key=lambda event: event["timestamp"]
    )
