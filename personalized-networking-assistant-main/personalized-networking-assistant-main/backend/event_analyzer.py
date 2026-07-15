from transformers import pipeline

# Zero-shot classification pipeline
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

CANDIDATE_LABELS = [
    "Artificial Intelligence",
    "Sustainability",
    "Healthcare",
    "Technology",
    "Education",
    "Finance",
    "Blockchain",
    "Urban Planning",
    "Climate Change",
    "Networking"
]

def analyze_event(event_description):
    result = classifier(
        event_description,
        candidate_labels=CANDIDATE_LABELS
    )

    themes = result["labels"][:3]
    return themes


# Test
if __name__ == "__main__":
    event = "AI for Sustainable Cities and Urban Planning"
    themes = analyze_event(event)
    print("Detected Themes:", themes)