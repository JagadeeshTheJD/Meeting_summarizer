# AI-Powered Meeting Summarization

This project provides an AI-powered meeting transcription and summarization system using FastAPI for the backend and Streamlit for the frontend. The system transcribes audio, refines the transcription, and generates structured summaries with key discussions, decisions made, and action items.

---

## 🛠 Setup Instructions

### 1️⃣ Install Dependencies
Ensure you have Python installed, then install the required dependencies:
```sh
pip install -r requirements.txt
```

### 2️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and add the following:
```sh
GROQ_API_KEY=your_groq_api_key_here
```
Replace `your_groq_api_key_here` with your actual API key from Groq.

---

## 🚀 Running the Application

### 1️⃣ Start the FastAPI Backend
Run the following command to start the backend:
```sh
uvicorn apibackend:app --reload
```
This will start the FastAPI server at `http://127.0.0.1:8000`.

### 2️⃣ Start the Streamlit Frontend
Open another terminal and run:
```sh
streamlit run app.py
```
This will launch the Streamlit UI for uploading audio files and viewing the transcriptions and summaries.

---

## 📂 Project Structure
```
📂 project_root/
│-- apibackend.py      # FastAPI backend for processing audio
│-- app.py             # Streamlit frontend for user interaction
│-- .env               # Environment variables (GROQ_API_KEY)
│-- requirements.txt   # Required dependencies
│-- README.md          # This file
|-- audio.mp3          # sample audio file
```

---

## 🎯 Features
✅ **Audio Transcription** using Distil-Whisper 
✅ **Refined Transcription** for better accuracy
✅ **Structured Summarization** with Mixtral-8x7b-32768
✅ **User-friendly Interface** with Streamlit
✅ **FastAPI Backend** for efficient processing

---

## 📝 Notes
- Make sure your `.env` file is correctly set up.
- If you face authentication issues, ensure your Groq API key is valid.
- Use supported audio formats (`wav`, `mp3`, `m4a`, `ogg`, `flac`).

---



**Lot of updates comming in this repo,realy excited.**
