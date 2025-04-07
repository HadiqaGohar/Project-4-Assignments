import streamlit as st
import string
import random
from graph import Graph, Vertex

# Function to extract words from text
def extract_word(text):
    try:
        text = text.decode('utf-8')
    except UnicodeDecodeError:
        st.error("Unable to decode the text. Please ensure the file is in UTF-8 format. 📄🚫")
        return []
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words if words else []

# Function to build a graph
def build_graph(words):
    if not words:
        st.error("No words found in the text. 😔")
        return None

    graph = Graph()
    prev_vertex = None

    for word in words:
        word_vertex = graph.get_vertex(word)
        if prev_vertex:
            graph.add_edge(prev_vertex, word_vertex)
        prev_vertex = word_vertex

    graph.generate_probability_mapping()
    return graph

# Function to generate formatted text from the graph
def generate_text(graph, words):
    if not words or not graph:
        st.error("No words or graph available for text generation. 🛑")
        return ""

    formatted_text = "\n".join(words)
    return formatted_text

# Streamlit app starts here
st.title("Markov Chain Text Generator 🧠🔀")

uploaded_files = st.file_uploader("Upload text file(s) 📂", type=["txt"], accept_multiple_files=True)

all_words = []

for file in uploaded_files or []:
    all_words.extend(extract_word(file.read()))

if all_words:
    st.success(f"Processed {len(uploaded_files)} file(s)! 🎉")
    graph = build_graph(all_words)

    if st.button("Generate Text ✨"):
        st.subheader("Generated Text ✍️")
        st.markdown(generate_text(graph, all_words))
else:
    st.info("Upload at least one text file to generate text. 📥")

# Footer
st.markdown("---")
st.caption("🔧 Built with love by **Hadiqa Gohar** ❤️")
