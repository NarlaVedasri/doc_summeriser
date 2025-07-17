

📝 GROQ Document Summarizer with LLaMA3 – Powered by Streamlit

📌 Project Overview

This Streamlit app allows you to upload PDF or TXT files and instantly get a structured, AI-generated summary using Groq’s LLaMA3 model.

Built for speed and simplicity, it delivers clean, readable summaries with just one click.


🚀 How to Use It (Local Setup)

1. Clone the repository

git clone https://github.com/NarlaVedasri/doc_summeriser.git
cd doc_summeriser
2. Install dependencies


pip install -r requirements.txt

 3. Set your Groq API key

Create a `.env` file and add your key:

GROQ_API_KEY=your_actual_groq_api_key_here
4. Run the app


streamlit run docsummarizer.py


🧠 What It Can Do

✅ Upload PDF or TXT files
✅ Use LLaMA3 via Groq API for blazing-fast document summarization
✅ Clean and concise summary output
✅ Option to download the summary as `.txt`
✅ Built with Streamlit – easy and lightweight UI



 📁 Project Structure


📦 doc_summeriser
┣ 📄 docsummarizer.py         # Main Streamlit app
┣ 📄 requirements.txt         # Python dependencies
┣ 📄 .env                     # Stores Groq API Key (not uploaded to GitHub)
┣ 📄 README.md                # You're reading it!
┣ 📄 LICENSE                  # MIT License


✨ Tech Stack

Streamlit – Interactive web app
Groq API– LLaMA3 for summarization
LangChain – Document loaders and chunking
dotenv – Secure API key handling



 👩‍💻 Created By

Vedasri Narla



📄 License

This project is licensed under the [MIT License](LICENSE).




