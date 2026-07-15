from fastapi import FastAPI
from backend.event_analyzer import analyze_event
from backend.topic_generator import generate_conversation_starters
from backend.fact_checker import fact_check

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Personalized Networking Assistant API"}


@app.post("/analyze-event")
def analyze(event_description: str):

    themes = analyze_event(event_description)

    return {
        "themes": themes
    }


@app.post("/generate-conversation")
def generate(event_description: str):

    themes = analyze_event(event_description)

    starters = generate_conversation_starters(themes)

    return {
        "themes": themes,
        "conversation_starters": starters
    }


@app.get("/fact-check")
def verify(topic: str):

    result = fact_check(topic)

    return {
        "topic": topic,
        "summary": result
    }