def deduplicate(events):

    unique = []

    seen = set()

    for event in events:

        key = str(event)

        if key not in seen:

            seen.add(key)

            unique.append(event)

    return unique
