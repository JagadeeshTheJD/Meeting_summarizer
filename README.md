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

## 📂 Project Structure
    📂 project_root/
    │-- apiftest.py        # FastAPI backend for processing audio and summarization
    │-- app.py             # Streamlit frontend for user interaction
    │-- .env               # Environment variables (GROQ_API_KEY)
    │-- requirements.txt   # Required dependencies
    │-- README.md          # This file
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
