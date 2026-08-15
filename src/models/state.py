from dataclasses import dataclass
from dataclasses import field


@dataclass
class State:

    timestamp: str = ""

    processes: dict = field(
        default_factory=dict
    )

    files: dict = field(
        default_factory=dict
    )

    users: dict = field(
        default_factory=dict
    )

    def to_dict(self):

        return {

            "timestamp":
            self.timestamp,

            "processes":
            self.processes,

            "files":
            self.files,

            "users":
            self.users
        }
