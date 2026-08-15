from pathlib import Path

from src.parsers.audit_parser import AuditParser
from src.parsers.dmesg_parser import DmesgParser
from src.parsers.kernel_parser import KernelParser


class LogLoader:

    def __init__(self, log_directory="logs"):

        self.log_directory = Path(log_directory)

        self.parsers = {
            "audit.log": AuditParser(),
            "dmesg.log": DmesgParser(),
            "kernel_module.log": KernelParser()
        }

    def load_logs(self):

        events = []

        for filename, parser in self.parsers.items():

            filepath = self.log_directory / filename

            if not filepath.exists():

                print(f"Warning: {filepath} not found")

                continue

            events.extend(parser.parse(filepath))

        return events


def load_logs(log_directory="logs"):

    loader = LogLoader(log_directory)

    return loader.load_logs()
