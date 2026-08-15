from dataclasses import dataclass
from typing import Dict
from typing import Any


@dataclass(frozen=True)
class Event:

    event_id: str

    timestamp: str

    source: str

    event_type: str

    details: Dict[str, Any]
