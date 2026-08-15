
import unittest

from src.models.event import Event
from src.engine.deduplicator import remove_duplicates


class TestDeduplication(unittest.TestCase):

    def test_duplicate_events(self):

        event1 = Event(

            event_id="1",

            timestamp="2026-08-15T10:00:00Z",

            source="audit",

            event_type="process_start",

            details={"pid": 100}
        )

        event2 = Event(

            event_id="2",

            timestamp="2026-08-15T10:00:00Z",

            source="audit",

            event_type="process_start",

            details={"pid": 100}
        )

        events = [event1, event2]

        unique_events = remove_duplicates(events)

        self.assertEqual(

            len(unique_events),

            1
        )


if __name__ == "__main__":

    unittest.main()
