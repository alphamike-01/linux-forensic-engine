from src.detectors.file_detector import detect_file_tampering

from src.detectors.privilege_detector import detect_privilege_escalation


def test_privilege_escalation():

    anomalies = detect(
        old_role="user",
        new_role="root"
    )

    assert len(anomalies) == 1

    assert anomalies[0]["type"] == (
        "privilege_escalation"
    )
