import streamlit as st

# Set up page with wide layout
st.set_page_config(page_title="Jalrakshak Interactive Prototype", layout="wide")

# Inject custom CSS to remove padding from the main Streamlit content block
st.markdown("""
<style>
    /* Target the main content container and remove padding */
    .st-emotion-cache-z5fcl4 { /* This is often the main content container class in newer Streamlit versions */
        padding: 0px;
    }
    .main .block-container { /* A common older class for the main content container */
        padding-top: 0rem;
        padding-right: 0rem;
        padding-left: 0rem;
        padding-bottom: 0rem;
        margin: 0rem;
    }
</style>
""", unsafe_allow_html=True)


# Read the HTML file
with open("chatbot.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Embed the HTML inside Streamlit
# You might still need to adjust the height/width of the iframe itself
st.components.v1.html(html_code, height=1000, width=None) 
# Set scrolling to False if you want the content in the HTML to handle its own scrolling
# st.markdown(html_code, unsafe_allow_html=True)
