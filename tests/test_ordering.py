import unittest

from src.models.event import Event
from src.engine.reconciler import reconcile


class TestOrdering(unittest.TestCase):

    def test_event_ordering(self):

        event1 = Event(

            event_id="1",

            timestamp="2026-08-15T10:00:05Z",

            source="audit",

            event_type="process_start",

            details={}
        )

        event2 = Event(

            event_id="2",

            timestamp="2026-08-15T10:00:01Z",

            source="kernel_module",

            event_type="file_access",

            details={}
        )

        ordered = reconcile(

            [event1, event2]
        )

        self.assertEqual(

            ordered[0].timestamp,

            "2026-08-15T10:00:01Z"
        )


if __name__ == "__main__":

    unittest.main()
