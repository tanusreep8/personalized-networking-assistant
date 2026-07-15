from transformers import pipeline

# Load GPT-2 model
generator = pipeline(
    "text-generation",
    model="gpt2"
)

def generate_conversation_starters(themes):

    prompt = (
        f"Generate 3 professional networking conversation starters "
        f"about {', '.join(themes)}."
    )

    result = generator(
        prompt,
        max_length=100,
        num_return_sequences=1
    )

    return result[0]["generated_text"]


# Test
if __name__ == "__main__":

    themes = [
        "Artificial Intelligence",
        "Technology",
        "Sustainability"
    ]

    starters = generate_conversation_starters(themes)

    print("\nGenerated Conversation Starters:\n")
    print(starters)