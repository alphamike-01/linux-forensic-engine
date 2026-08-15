import time

from ingest.loader import load_logs
from reconciliation.deduplicator import deduplicate
from reconciliation.sorter import order
from state.engine import reconstruct


def benchmark():

    start = time.perf_counter()

    events = load_logs()

    events = deduplicate(events)

    events = order(events)

    reconstruct(events)

    end = time.perf_counter()

    print(f"Execution time: {end-start:.3f} seconds")


if __name__ == "__main__":

    benchmark()
