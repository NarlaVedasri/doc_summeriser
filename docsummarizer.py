import streamlit as st
import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq Chat Client with LLaMA3
llm = ChatGroq(api_key=GROQ_API_KEY, model_name="llama3-8b-8192")

# Streamlit app layout
st.set_page_config(page_title="📝 Groq Document Summarizer", layout="centered")
st.title("📝 Groq Document Summarizer using LLaMA3")

# Upload file (PDF or TXT)
uploaded_file = st.file_uploader("Upload your document (PDF or TXT)", type=["pdf", "txt"])

# Define summarization prompt
summary_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
    Summarize the following document in clear bullet points.

    Document:
    {text}

    Summary:
    """
)

# Function to extract and load file content
def load_file(file):
    with open(file.name, "wb") as f:
        f.write(file.getbuffer())
    if file.name.endswith(".pdf"):
        return PyPDFLoader(file.name).load()
    else:
        return TextLoader(file.name).load()

# Main logic after file upload
if uploaded_file:
    st.success(f"✅ Uploaded: {uploaded_file.name}")

    # Load and split the document
    docs = load_file(uploaded_file)
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(docs)

    st.info("⏳ Summarizing document with LLaMA3 via Groq...")
    summary_output = ""

    for chunk in chunks:
        prompt = summary_prompt.format(text=chunk.page_content)
        response = llm.invoke(prompt)
        summary_output += response.content.strip() + "\n\n"

    # Show the summary
    st.subheader("📄 Document Summary")
    st.write(summary_output)

    # Allow summary download
    st.download_button(
        label="📥 Download Summary as .txt",
        data=summary_output,
        file_name="document_summary.txt",
        mime="text/plain"
    )
else:
    st.info("📂 Upload a document to generate its summary.")
