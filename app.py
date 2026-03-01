import streamlit as st
from services.llm_service import LLMService
from services.classroom_service import get_courses, get_assignments
from utils.prompts import SYSTEM_PROMPT

st.set_page_config(page_title="C++ AI Assistant", layout="wide")

st.title("💻 C++ AI Assistant")
st.markdown("AI Tutor for C++ Programming + Google Classroom Integration")

# Initialize LLM
llm = LLMService()

# Sidebar
st.sidebar.header("Google Classroom")

if st.sidebar.button("Load My Courses"):
    try:
        courses = get_courses()
        for course in courses:
            st.sidebar.write(f"📚 {course['name']}")
    except Exception as e:
        st.sidebar.error("Google Classroom not configured properly.")

# Chat Section
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask anything about C++...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = llm.generate_response(user_input, SYSTEM_PROMPT)

    st.session_state.messages.append({"role": "assistant", "content": response})

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
