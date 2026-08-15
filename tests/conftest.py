import json
from pathlib import Path


def load_fixture(filename):

    path = Path("tests/fixtures") / filename

    with open(path) as f:

        return json.load(f)
