import time


def test_performance():

    events = generate_events(
        count=10000
    )

    start = time.time()

    process_events(events)

    duration = (
        time.time() - start
    )

    assert duration < 10
