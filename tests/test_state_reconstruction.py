from src.engine.state_engine import apply_event


def test_process_creation():

    state = create_empty_state()

    event = create_process_event(
        pid=100,
        exe="/bin/bash"
    )

    new_state = apply_event(
        state,
        event
    )

    assert 100 in new_state.processes
