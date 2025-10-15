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

The project leverages **Groq AI models** and **OpenAI Whisper** for audio-to-text, refinement, and summarization tasks.

### 1️⃣ Whisper (local)
- Developed by OpenAI.  
- Performs **speech-to-text transcription** locally for free.  
- Handles multiple languages and noisy environments effectively.  
- Used for converting meeting audio into text.

### 2️⃣ Llama-3.1-8b-instant
- A fast, efficient **Groq LLM** optimized for real-time responses.  
- Used for **refinement** of transcriptions — fixing grammar, missing words, and improving coherence.  
- Ensures the meaning is preserved while improving readability.

### 3️⃣ Llama-3.3-70b-versatile
- A large, powerful **Groq LLM** used for **structured summarization**.  
- Generates key discussion points, decisions made, and actionable tasks.  
- Provides concise, organized summaries for better understanding.

Together, these models ensure accurate transcriptions and meaningful, structured summaries with minimal human intervention.

---

## 📂 Project Structure
    📂 Meeting_summarizer/
    │-- apiftest.py        # FastAPI backend for processing audio and summarization
    │-- app.py             # Streamlit frontend for user interaction
    │-- main.py            # Local Whisper + Summarization alternative pipeline
    │-- requirements.txt   # Required dependencies
    │-- .env               # Environment variables (GROQ_API_KEY)
    │-- README.md          # Project documentation

---

## 🎯 Features
✅ **Automatic Audio Transcription** using Whisper  
✅ **Refined Transcription** with Llama-3.1-8b-instant  
✅ **Structured Summarization** via Llama-3.3-70b-versatile  
✅ **FastAPI Backend** for modular and scalable processing  
✅ **Streamlit Frontend** for easy interaction and output visualization  
✅ **Multi-format Support** for various audio files  

---

## 🧩 Supported Audio Formats
`wav`, `mp3`, `m4a`, `ogg`, `flac`

---

## 🧠 Workflow Overview

1️⃣ User uploads an audio file through Streamlit.  
2️⃣ FastAPI backend saves and processes the file.  
3️⃣ Whisper model transcribes the audio into text.  
4️⃣ Llama-3.1-8b-instant refines the transcription.  
5️⃣ Llama-3.3-70b-versatile generates a structured summary.  
6️⃣ Streamlit displays the complete results to the user.

---

## ⚙️ Example API Response

```json
{
  "message": "✅ Audio processed successfully",
  "original_transcription": "Good morning everyone, let's start the meeting...",
  "refined_transcription": "Good morning everyone. Let’s begin today’s meeting...",
  "structured_summary": "### Summary\n- Discussed project milestones.\n### Key Decisions\n- Extended deadline by 2 weeks.\n### Action Items\n- Task: Update project plan\n  - Assigned to: Raj\n  - Due date: Oct 20"
}
