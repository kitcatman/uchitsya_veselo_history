import json
from pathlib import Path

def load_quests():
    json_path = Path(__file__).parent / "quests.json"

    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)