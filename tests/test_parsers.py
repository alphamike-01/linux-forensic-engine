from src.parsers.audit_parser import parse_audit


def test_missing_pid():

    line = (
        "type=SYSCALL "
        "msg=audit(2026-08-15T10:00:01Z): "
        "exe=/bin/bash "
        "uid=1000"
    )

    event = parse_audit_line(line)

    assert event is not None
