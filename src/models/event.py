from dataclasses import asdict
from dataclasses import dataclass
from typing import Any
from typing import Dict


@dataclass(frozen=True)
class Event:

    event_id: str

    timestamp: str

    source: str

    event_type: str

    details: Dict[str, Any]

    def to_dict(self):

        return asdict(self)
