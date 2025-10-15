import os
import logging
from fastapi import FastAPI, UploadFile, File, HTTPException
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Validate API Key
if not GROQ_API_KEY:
    raise ValueError("❌ Missing GROQ_API_KEY. Please check your .env file.")

# Initialize FastAPI app
app = FastAPI()

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    return {"message": "API is running successfully!"}

@app.post("/process-audio/")
async def process_audio(file: UploadFile = File(...)):
    """
    Process uploaded audio file:
    - Transcribes using Groq
    - Refines transcript for accuracy
    - Uses Mixtral-8x7b-32768 for structured summarization
    """
    try:
        # Validate file extension
        allowed_extensions = {"wav", "mp3", "m4a", "ogg", "flac"}
        file_extension = file.filename.split('.')[-1].lower()

        if file_extension not in allowed_extensions:
            raise HTTPException(status_code=400, detail=f"Unsupported file format: {file_extension}")

        logger.info(f"📂 Received file: {file.filename} ({file_extension})")

        # Transcribe the file
        try:
            transcription_response = client.audio.transcriptions.create(
                file=(file.filename, await file.read()),
                model="whisper-large-v3",
                response_format="json",
            )
            transcription = transcription_response.text.strip()  # 🔥 FIXED: Use .text instead of ["text"]
            logger.info("📝 Transcription completed")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Transcription failed: {str(e)}")

        # **Step 1: Refine Transcription**
        refinement_prompt = (
            "You are an AI assistant that improves raw transcriptions. "
            "Your task is to correct missing words, fix incomplete sentences,"
            "like  A.A actualy means AI and PowerD measn powered "
            "and ensure coherence while keeping the original meaning. "
            "Do not change technical terms or speaker context.\n\n"
            "Here is the raw transcript:\n\n" + transcription
        )

        try:
            refined_response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "system", "content": "You are a professional transcription editor."},
                          {"role": "user", "content": refinement_prompt}],
                max_tokens=4000
            )
            refined_transcription = refined_response.choices[0].message.content.strip()
            logger.info("📝 Transcription refinement completed")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Refinement failed: {str(e)}")

        # **Step 2: Structured Summarization**
        summary_prompt = (
            "Analyze the refined transcript and extract key insights:\n\n"
            "## summary \n - what happened , whom joined and what happened in simple terms"
            "### Key Discussions\n- Identify the main topics discussed.\n\n"
            "### Decisions Made\n- List the key decisions agreed upon.\n\n"
            "### Action Items\n- Task: [Task description]\n  - Assigned to: [Person/Team]\n  - Due date: [Optional]\n\n"
            "Ensure a structured response using bullet points."
        )

        try:
            summary_response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": "You are an AI assistant summarizing a transcript."},
                          {"role": "user", "content": summary_prompt + "\n\n" + refined_transcription}],
                max_tokens=2000
            )
            structured_summary = summary_response.choices[0].message.content.strip()
            logger.info("📋 Structured summarization completed")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Summarization failed: {str(e)}")

        return {
            "message": "✅ Audio processed successfully",
            "original_transcription": transcription,
            "refined_transcription": refined_transcription,
            "structured_summary": structured_summary
        }
    
    except Exception as e:
        logger.error(f"❌ Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

