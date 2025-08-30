import whisper
from moviepy.editor import VideoFileClip
import os
import sys

AUDIO_FORMATS = [".mp3", ".wav", ".m4a", ".flac", ".aac"]
VIDEO_FORMATS = [".mp4", ".mov", ".avi", ".mkv"]
SUPPORTED_FORMATS = AUDIO_FORMATS + VIDEO_FORMATS

def extract_audio(video_path, audio_path="temp_audio.wav"):
    try:
        video = VideoFileClip(video_path)
        if not video.audio:
            print("[ERROR] No audio track found.")
            sys.exit(1)
        video.audio.write_audiofile(audio_path, logger=None)
        video.close()
        return audio_path
    except Exception as e:
        print(f"[ERROR] Audio extraction failed: {e}")
        sys.exit(1)

def transcribe_audio(audio_path):
    try:
        print("[INFO] Loading Whisper model...")
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        print(f"[ERROR] Transcription failed: {e}")
        sys.exit(1)

def transcribe_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext in AUDIO_FORMATS:
        return transcribe_audio(file_path)
    elif ext in VIDEO_FORMATS:
        audio_path = extract_audio(file_path)
        text = transcribe_audio(audio_path)
        os.remove(audio_path)
        return text
    else:
        print(f"[ERROR] Unsupported file format: {ext}")
        sys.exit(1)

# 🔽 Just change this path to your uploaded file
file_path = "your_uploaded_file.mp4"  # Replace with your actual file path

if not os.path.exists(file_path):
    print("[ERROR] File not found.")
    sys.exit(1)

print("\n🔍 Transcribing now...\n")
text = transcribe_file(file_path)
print("\n📝 [TRANSCRIPTION RESULT]:\n")
print(text)

# Optional: Save to file
output_file = os.path.splitext(file_path)[0] + "_transcription.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)
print(f"\n✅ Saved to {output_file}")
