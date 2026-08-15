# Linux Event Stream Reconciliation and State Reconstruction Engine for Forensic Analysis

## Features

- Audit log parsing
- dmesg parsing
- Kernel module parsing
- Event deduplication
- Event reconciliation
- Immutable state reconstruction
- Conflict resolution
- Privilege escalation detection
- File tampering detection
- Replay API
- JSON export

## Installation

```bash
git clone <repository_url>

cd linux-forensic-engine

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Run API

```bash
python -m src.api.server
```

## Run Tests

```bash
python3 -m unittest discover tests
```

## Project Structure

- `logs/` → input logs
- `output/` → generated files
- `src/` → source code
- `tests/` → automated tests
