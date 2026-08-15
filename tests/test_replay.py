def test_replay_is_deterministic():

    state1 = process_events()

    state2 = process_events()

    assert state1 == state2

def test_idempotency():

    state1 = process_events()

    state2 = process_events()

    assert state1 == state2
