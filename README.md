# Meeting Summarizer

This project provides an **AI-powered meeting transcription and summarization system** using **FastAPI** for the backend and **Streamlit** for the frontend.  
The system transcribes audio, refines the transcription, and generates structured summaries with key discussions, decisions made, and action items.

---

## 🛠 Setup Instructions

### 1️⃣ Install Dependencies
Ensure you have Python (3.9 or above) installed, then install the required dependencies:

    pip install -r requirements.txt

### 2️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and add the following:

    GROQ_API_KEY=your_groq_api_key_here

Replace `your_groq_api_key_here` with your actual API key from [Groq](https://console.groq.com/).

---

## 🚀 Running the Application

### 1️⃣ Start the FastAPI Backend
Run the following command to start the backend:

    uvicorn apiftest:app --reload

This will start the FastAPI server at `http://127.0.0.1:8000`.

### 2️⃣ Start the Streamlit Frontend
Open another terminal and run:

    streamlit run app.py

This will launch the Streamlit UI for uploading audio files and viewing the transcriptions and summaries.

---

## 🤖 Models Used

The project leverages **Groq AI models** for audio-to-text, refinement, and summarization tasks.

1️⃣ **Whisper-large-v3**  
   - Developed by OpenAI.  
   - Performs **speech-to-text transcription** with high accuracy.  
   - Handles multiple languages and background noise effectively.  
   - Used for converting raw meeting audio into text.

2️⃣ **Llama-3.1-8b-instant**  
   - A large language model optimized for **fast inference and lightweight summarization**.  
   - Used for **transcription refinement** — fixing grammar, incomplete phrases, and coherence while preserving meaning.

3️⃣ **Llama-3.3-70b-versatile**  
   - A powerful LLM used for **structured summarization**.  
   - Generates key points, decisions made, and actionable insights.  
   - Ensures the summary is concise, readable, and logically structured.

These models together ensure the system provides accurate transcriptions and meaningful summaries with minimal human intervention.

---

## 📂 Project Structure
    📂 project_root/
    │-- apiftest.py        # FastAPI backend for processing audio and summarization
    │-- app.py             # Streamlit frontend for user interaction
    │-- .env               # Environment variables (GROQ_API_KEY)
    │-- requirements.txt   # Required dependencies
    │-- audio.mp3          # Sample audio file

---

## 🎯 Features
✅ **Audio Transcription** using Whisper-large-v3  
✅ **Refined Transcription** for improved grammar and coherence  
✅ **Structured Summarization** using Llama-3.3-70b-versatile  
✅ **FastAPI Backend** for efficient and modular processing  
✅ **Streamlit Frontend** for an easy-to-use interface  

---

## 🧩 Supported Audio Formats
`wav`, `mp3`, `m4a`, `ogg`, `flac`

---

## 📝 Notes
- Ensure your `.env` file is correctly set up with a valid **Groq API key**.  
- Always start the backend before launching the Streamlit app.  
- For best performance, keep audio clips under **5 minutes**.  

---

**Lot of updates coming in this repo — really excited! 🎉**
