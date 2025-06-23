import streamlit as st
import string
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Word Count Tool",
    page_icon="📝",
    layout="centered"
)

# Add custom styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .title {
        text-align: center;
        font-size: 2.2em;
        color: #4CAF50;
    }
    .footer {
        text-align: center;
        color: #888;
        font-size: 0.9em;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">📝 Word Count Dictionary Generator</div>', unsafe_allow_html=True)
st.caption("Created by **Prasad Parjane** | Demo Project")

# Description
st.write("Paste or type your paragraph below.")
st.write(" Click **Get Word Counts** to see how many times each word appears")
# Input area
paragraph = st.text_area("✍️ Enter your paragraph here:", height=200)

# Button
if st.button("🔍 Get Word Counts"):
    if paragraph.strip():
        # Clean text
        translator = str.maketrans('', '', string.punctuation)
        cleaned = paragraph.translate(translator).lower()
        words = cleaned.split()

        # Count words
        word_counts = {word: words.count(word) for word in set(words)}

        # Display as table
        df = pd.DataFrame(list(word_counts.items()), columns=['Word', 'Count']).sort_values(by='Count', ascending=False).reset_index(drop=True)
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("⚠️ Please enter some text to analyze.")

# Footer
st.markdown('<div class="footer">© 2025 Prasad Parjane</div>', unsafe_allow_html=True)
