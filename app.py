import streamlit as st

# Set up page
st.set_page_config(page_title="Jalrakshak Interactive Prototype", layout="centered")

st.markdown("<h2 style='text-align:center;'>💧 Jalrakshak Interactive Prototype</h2>", unsafe_allow_html=True)

# Read the HTML file
with open("chatbot.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Embed the HTML inside Streamlit
st.components.v1.html(html_code, height=800, scrolling=True)
