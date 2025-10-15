import os
import logging
import tempfile
from fastapi import FastAPI, UploadFile, File, HTTPException
from dotenv import load_dotenv
from groq import Groq
import whisper

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
    return {"message": "🚀 API is running successfully!"}


@app.post("/process-audio/")
async def process_audio(file: UploadFile = File(...)):
    """
    Process uploaded audio file:
    - Transcribes using local Whisper (offline)
    - Refines transcript using Groq (llama-3.1-8b-instant)
    - Summarizes using Groq (llama-3.3-70b-versatile)
    """
    try:
        # ✅ Step 1: Validate file
        allowed_extensions = {"wav", "mp3", "m4a", "ogg", "flac"}
        file_extension = file.filename.split(".")[-1].lower()

        if file_extension not in allowed_extensions:
            raise HTTPException(status_code=400, detail=f"Unsupported file format: {file_extension}")

        logger.info(f"📂 Received file: {file.filename} ({file_extension})")

        # ✅ Step 2: Save file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_extension}") as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        # ✅ Step 3: Transcribe using local Whisper
        try:
            model = whisper.load_model("small")
            result = model.transcribe(tmp_path)
            transcription = result["text"].strip()
            logger.info("📝 Transcription completed successfully")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Local transcription failed: {str(e)}")
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

        # ✅ Step 4: Refine transcription using Groq
        refinement_prompt = (
            "You are an AI assistant that improves raw transcriptions. "
            "Fix incomplete sentences, spelling mistakes, and interpret short forms "
            "(e.g., 'A.A' means 'AI', 'PowerD' means 'powered'). "
            "Ensure clarity and readability while preserving meaning.\n\n"
            "Here is the raw transcript:\n\n" + transcription
        )

        try:
            refined_response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are a professional transcription editor."},
                    {"role": "user", "content": refinement_prompt}
                ],
                max_tokens=4000
            )
            refined_transcription = refined_response.choices[0].message.content.strip()
            logger.info("✨ Transcription refinement completed")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Refinement failed: {str(e)}")

        # ✅ Step 5: Summarize using Groq
        summary_prompt = (
            "Analyze the refined transcript and provide a structured meeting summary:\n\n"
            "## Summary\n- Describe what happened, who participated, and key events.\n\n"
            "### Key Discussions\n- List the main discussion points.\n\n"
            "### Decisions Made\n- List important decisions or conclusions.\n\n"
            "### Action Items\n- Task: [Task description]\n  - Assigned to: [Person/Team]\n  - Due date: [Optional]\n\n"
            "Format clearly using bullet points."
        )

        try:
            summary_response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are an AI assistant summarizing a meeting transcript."},
                    {"role": "user", "content": summary_prompt + "\n\n" + refined_transcription}
                ],
                max_tokens=2000
            )
            structured_summary = summary_response.choices[0].message.content.strip()
            logger.info("📋 Structured summarization completed")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Summarization failed: {str(e)}")

        # ✅ Step 6: Return results
        return {
            "message": "✅ Audio processed successfully",
            "original_transcription": transcription,
            "refined_transcription": refined_transcription,
            "structured_summary": structured_summary
        }

    except Exception as e:
        logger.error(f"❌ Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
