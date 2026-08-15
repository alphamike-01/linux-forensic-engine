from src.parsers.audit_parser import parse_audit
from src.parsers.dmesg_parser import parse_dmesg
from src.parsers.kernel_parser import parse_kernel

from src.engine.deduplicator import remove_duplicates
from src.engine.reconciler import reconcile
from src.engine.state_engine import apply_event

from src.models.state import State
from src.detectors.privilege_detector import (
    detect_privilege_escalation
)

from src.detectors.file_detector import (
    detect_file_tampering
)

from src.engine.audit_engine import (
    record,
    get_audit_trail
)


# Load events from all log sources

events = []

events.extend(
    parse_audit(
        "logs/audit.log"
    )
)

events.extend(
    parse_dmesg(
        "logs/dmesg.log"
    )
)

events.extend(
    parse_kernel(
        "logs/kernel_module.log"
    )
)


# Remove duplicate events

events = remove_duplicates(events)


# Sort events

events = reconcile(events)


state = State()

snapshots = []


for event in events:

    anomalies = []

    privilege = (
        detect_privilege_escalation(
            event
        )
    )

    if privilege:

        anomalies.append(
            privilege
        )

    file_alert = (
        detect_file_tampering(
            event
        )
    )

    if file_alert:

        anomalies.append(
            file_alert
        )

    previous_state = state

    state = apply_event(
        state,
        event
    )

    snapshots.append(
        state
    )

    record(
        event,
        anomalies,
        []
    )

# Display the reconstructed state

print("\nProcesses:\n")

print(state.processes)

print("\nFiles:\n")

print(state.files)

print("\nUsers:\n")

print(state.users)

print("\nANOMALIES\n")

for audit in get_audit_trail():

    if audit["anomalies"]:

        print(audit)
