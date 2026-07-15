import json
import os

FEEDBACK_FILE = "data/feedback.json"

def save_feedback(starter, feedback):

    record = {
        "starter": starter,
        "feedback": feedback
    }

    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r") as file:
            try:
                data = json.load(file)
            except:
                data = []
    else:
        data = []

    data.append(record)

    with open(FEEDBACK_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print("Feedback saved successfully!")


if __name__ == "__main__":

    save_feedback(
        "How do you see AI helping cities?",
        "thumbs_up"
    )