from src.engine.conflict_resolver import resolve_conflict


def test_conflicting_permissions():

    event1 = {
        "source": "audit",
        "permission": "644",
        "timestamp": 1,
        "pid": 200
    }

    event2 = {
        "source": "kernel_module",
        "permission": "777",
        "timestamp": 2,
        "pid": 100
    }

    winner = resolve(event1, event2)

    assert winner["permission"] == "777"
