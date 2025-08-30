import os
import math
import datetime
import moviepy.editor as mp
from transformers import pipeline
import google.generativeai as genai

# -----------------------------
# CONFIGURE GEMINI
# -----------------------------
API_KEY = "AIzaSyBtjp5KA_0sbfRXxAmF62-Pp0AlyTB90-0"   # Replace with your Gemini API key
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# -----------------------------
# SETUP WHISPER ASR (for transcription)
# -----------------------------
asr = pipeline("automatic-speech-recognition", model="openai/whisper-small")

# -----------------------------
# Split video into chunks
# -----------------------------
def split_video(video_path, chunk_length=20*60):
    video = mp.VideoFileClip(video_path)
    duration = int(video.duration)
    return [(start, min(start+chunk_length, duration)) for start in range(0, duration, chunk_length)]

# Convert seconds to timestamp
def format_timestamp(seconds):
    return str(datetime.timedelta(seconds=int(seconds)))

# Extract audio
def extract_audio(video_path, start, end, output_audio):
    video = mp.VideoFileClip(video_path).subclip(start, end)
    video.audio.write_audiofile(output_audio, codec="mp3")
    return output_audio

# Transcribe + Summarize
def analyze_chunk(audio_path, start, end):
    # Step 1: Transcribe with Whisper
    text = asr(audio_path)["text"]

    # Step 2: Summarize with Gemini
    prompt = f"Summarize the following transcript into clear bullet points:\n\n{text}"
    response = model.generate_content(prompt)
    summary = response.text if response and response.text else "No summary."

    return {
        "start": format_timestamp(start),
        "end": format_timestamp(end),
        "summary": summary
    }

# -----------------------------
# MAIN PIPELINE
# -----------------------------
def process_video(video_path, output_file="video_summary.txt"):
    results = []
    chunks = split_video(video_path)

    for i, (start, end) in enumerate(chunks):
        print(f"Processing chunk {i+1}: {format_timestamp(start)} - {format_timestamp(end)}")
        audio_file = f"chunk_{i+1}.mp3"
        extract_audio(video_path, start, end, audio_file)

        summary = analyze_chunk(audio_file, start, end)
        results.append(summary)
        os.remove(audio_file)

    # Save to file
    with open(output_file, "w", encoding="utf-8") as f:
        for i, res in enumerate(results):
            f.write(f"Chunk {i+1} ({res['start']} - {res['end']}):\n")
            f.write(res['summary'] + "\n\n")
    
    print(f"\n✅ Summary saved to {output_file}")


if __name__ == "__main__":
    video_path = "GMT20250824-081719_Recording_1920x1200.mp4"
    process_video(video_path)
