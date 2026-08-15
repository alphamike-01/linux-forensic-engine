import unittest

from src.models.event import Event
from src.detectors.privilege_detector import (
    detect_privilege_escalation
)


class TestPrivileges(unittest.TestCase):

    def test_root_detection(self):

        event = Event(

            event_id="1",

            timestamp="2026-08-15T10:00:00Z",

            source="audit",

            event_type="process_start",

            details={

                "uid": 0
            }
        )

        result = (

            detect_privilege_escalation(

                event
            )
        )

        self.assertIsNotNone(

            result
        )


if __name__ == "__main__":

    unittest.main()
