import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
from backend.event_analyzer import analyze_event
from backend.topic_generator import generate_conversation_starters
from backend.fact_checker import fact_check

st.title("Personalized Networking Assistant")

event_description = st.text_area(
    "Enter Event Description"
)

if st.button("Generate Conversation Starters"):

    themes = analyze_event(event_description)

    starters = generate_conversation_starters(themes)

    st.subheader("Detected Themes")
    st.write(themes)

    st.subheader("Conversation Starters")
    st.write(starters)

st.divider()

topic = st.text_input("Fact Check Topic")

if st.button("Fact Check"):

    result = fact_check(topic)

    st.subheader("Wikipedia Summary")
    st.write(result)