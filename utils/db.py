import json
import sys
import os

# LOADING THE CONFIG.JSON
if not os.path.isfile("config.json"):
    try:
        config = json.load(open("config.json", "r", encoding="utf-8"))
        print("Loaded the 'config.json' file")
    except FileNotFoundError:
        sys.exit("'config.json' file could not be detected!")
    except Exception as e:
        sys.exit(f"Error: {e}")
else:
    sys.exit("'config.json' file could not be detected!")
