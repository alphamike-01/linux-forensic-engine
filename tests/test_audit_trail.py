def test_audit_record_generation():

    audit_record = generate_audit_record()

    assert "event_id" in audit_record

    assert "state_changes" in audit_record

    assert "timestamp" in audit_record
