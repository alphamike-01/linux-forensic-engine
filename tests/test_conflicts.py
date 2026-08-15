import unittest

from src.models.event import Event
from src.engine.conflict_resolver import resolve_conflict


class TestConflicts(unittest.TestCase):

    def test_source_priority(self):

        audit_event = Event(

            event_id="1",

            timestamp="2026-08-15T10:00:00Z",

            source="audit",

            event_type="file_permission",

            details={

                "pid": 100,

                "path": "/etc/passwd",

                "action": "644"
            }
        )

        kernel_event = Event(

            event_id="2",

            timestamp="2026-08-15T10:00:00Z",

            source="kernel_module",

            event_type="file_permission",

            details={

                "pid": 100,

                "path": "/etc/passwd",

                "action": "777"
            }
        )

        winner = resolve_conflict(

            audit_event,

            kernel_event
        )

        self.assertEqual(

            winner.source,

            "kernel_module"
        )


if __name__ == "__main__":

    unittest.main()
