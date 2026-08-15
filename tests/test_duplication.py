from tests.conftest import load_fixture
from src.engine.deduplicator import remove_duplicates


def test_duplicate_events():

    events = load_fixture("duplicate_events.json")

    unique_events = deduplicate(events)

    assert len(unique_events) == 2
