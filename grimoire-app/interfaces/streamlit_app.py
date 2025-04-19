"""
streamlit_app.py

UI layer for the Streamlit app.
"""

import streamlit as st
from core.wisdom_engine import thought_routine_1, thought_routine_2, logic_handler_1, logic_handler_2
from services.gemini_agent import process_natural_language

def main():
    st.title("Grimoire App: Library of Living Wisdom")
    
    st.header("Thought Routines")
    input_data = st.number_input("Enter a number for thought routines:")
    if st.button("Run Thought Routine 1"):
        result = thought_routine_1(input_data)
        st.write(f"Result of Thought Routine 1: {result}")
    if st.button("Run Thought Routine 2"):
        result = thought_routine_2(input_data)
        st.write(f"Result of Thought Routine 2: {result}")
    
    st.header("Logic Handlers")
    if st.button("Run Logic Handler 1"):
        result = logic_handler_1(input_data)
        st.write(f"Result of Logic Handler 1: {result}")
    if st.button("Run Logic Handler 2"):
        result = logic_handler_2(input_data)
        st.write(f"Result of Logic Handler 2: {result}")
    
    st.header("Natural Language Processing")
    input_text = st.text_input("Enter text for natural language processing:")
    if st.button("Process Natural Language"):
        response = process_natural_language(input_text)
        st.write(f"Processed Text: {response}")

if __name__ == "__main__":
    main()
