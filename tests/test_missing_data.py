import unittest

from src.models.state import State
from src.engine.state_engine import apply_event
from src.models.event import Event


class TestMissingData(unittest.TestCase):

    def test_missing_pid(self):

        event = Event(

            event_id="1",

            timestamp="2026-08-15T10:00:00Z",

            source="kernel_module",

            event_type="file_access",

            details={

                "path": "/tmp/test",

                "action": "read"
            }
        )

        state = State()

        try:

            apply_event(

                state,

                event
            )

            success = True

        except Exception:

            success = False

        self.assertTrue(success)


if __name__ == "__main__":

    unittest.main()
