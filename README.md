# AIQoD_Hackathon

# Audio Processing API with Transcription, Refinement, and Summarization

This project provides an API for processing audio files. It transcribes the audio using Groq, refines the transcription for accuracy, and generates structured summaries of the content. The application uses FastAPI for the backend, Groq for transcription and refinement, and supports various audio file formats like `wav`, `mp3`, `m4a`, `ogg`, and `flac`.

## Features
- **Audio Transcription:** Transcribes the uploaded audio file to text.
- **Transcription Refinement:** Refines the raw transcription to improve accuracy and coherence.
- **Structured Summarization:** Generates a structured summary of the transcription, including key insights, discussions, decisions, and action items.

## Requirements

- Python 3.8 or higher
- Install dependencies using `pip install -r requirements.txt`

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AudioProcessingAPI.git
   cd AudioProcessingAPI
2. Create a .env file to store your GROQ API key:

  GROQ_API_KEY=your_api_key_here

3. Install the dependencies:
   
  pip install -r requirements.txt

4. Run the FastAPI app:

    uvicorn app:app --reload

5. Open the browser and go to http://127.0.0.1:8000/docs to view the interactive API documentation provided by FastAPI.

   
