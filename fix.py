import json

with open("CODE_FILE.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

# Fix or remove widgets metadata
if "widgets" in nb.get("metadata", {}):
    nb["metadata"]["widgets"] = {
        "application/vnd.jupyter.widget-state+json": {
            "state": {},
            "version_major": 2,
            "version_minor": 0
        }
    }

with open("CODE_FILE_FIXED.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=2)
