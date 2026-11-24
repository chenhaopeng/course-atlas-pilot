import json
from pathlib import Path


def load_topics():
    path = Path(__file__).parent / "data" / "topics.json"
    return json.loads(path.read_text(encoding="utf-8"))


def search(query):
    query = query.strip().casefold()
    return [
        topic["id"] for topic in load_topics()
        if query in {keyword.casefold() for keyword in topic["keywords"]}
    ]
