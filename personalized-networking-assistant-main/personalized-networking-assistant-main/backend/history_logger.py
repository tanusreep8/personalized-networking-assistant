import json
import os

HISTORY_FILE = "data/history.json"

def save_history(event, starter):

    record = {
        "event": event,
        "starter": starter
    }

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            try:
                history = json.load(file)
            except:
                history = []
    else:
        history = []

    history.append(record)

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)

    print("History saved successfully!")


# Test
if __name__ == "__main__":

    save_history(
        "AI for Sustainable Cities",
        "How do you see AI helping urban planning?"
    )