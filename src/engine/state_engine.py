import copy


def apply_event(

    current_state,

    event
):

    state = copy.deepcopy(
        current_state
    )

    state.timestamp = (
        event.timestamp
    )

    return state
