import streamlit as st
import requests

# Backend API URL
API_URL = "http://127.0.0.1:8000/process-audio/"

st.set_page_config(page_title="AI Meeting Summarizer", page_icon="🎙", layout="wide")

st.title("🎙 AI-Powered Meeting Transcription & Summarization")
st.write("Upload an audio file to get a **detailed transcription and structured summary**.")

# File upload
uploaded_file = st.file_uploader("📂 Upload an audio file", type=["wav", "mp3", "m4a", "ogg", "flac"])

if uploaded_file:
    st.audio(uploaded_file, format="audio/mp3")

    if st.button("🚀 Process Audio"):
        st.info("⏳ Uploading and processing the file...")

        files = {"file": (uploaded_file.name, uploaded_file.read(), "audio/mpeg")}

        try:
            response = requests.post(API_URL, files=files)

            if response.status_code == 200:
                data = response.json()
                st.success("✅ Processing complete!")

                # Display Original Transcription
                st.subheader("📝 Original Transcription (Before Refinement)")
                with st.expander("📜 Click to view raw transcription"):
                    st.write(data["original_transcription"])

                # Display Refined Transcription
                st.subheader("✨ Refined Transcription (Corrected)")
                with st.expander("📖 Click to view refined version"):
                    st.write(data["refined_transcription"])

                # Display Structured Summary
                st.subheader("📋 Structured Summary")
                st.markdown(data["structured_summary"])

            else:
                st.error(f"❌ Error: {response.json().get('detail', 'Unknown error')}")

        except requests.exceptions.RequestException as e:
            st.error(f"❌ Failed to connect to API: {str(e)}")