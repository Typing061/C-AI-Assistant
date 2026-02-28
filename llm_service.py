import streamlit as st
from groq import Groq


class LLMService:
    def __init__(self):
        self.client = Groq(
            api_key=st.secrets["GROQ_API_KEY"]
        )

    def generate_response(self, user_input, system_prompt):
        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.5,
        )

        return completion.choices[0].message.content