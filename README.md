# Video Timestamp Transcribe

A Python-based video transcription tool that provides both basic transcription and advanced timestamp-based summarization using Whisper ASR and Google Gemini AI.

## Features

- **Basic Transcription**: Convert video/audio files to text using OpenAI's Whisper model
- **Timestamp-based Summarization**: Split long videos into chunks and generate summaries with timestamps
- **Multiple Format Support**: Supports various video (MP4, MOV, AVI, MKV) and audio (MP3, WAV, M4A, FLAC, AAC) formats
- **AI-Powered Summaries**: Uses Google Gemini AI to create concise bullet-point summaries
- **Automatic Audio Extraction**: Extracts audio from video files for processing

## Files Overview

- `Transcribecode.py`: Basic video/audio transcription using Whisper
- `timestamp.py`: Advanced timestamp-based transcription with AI summarization

## Prerequisites

- Python 3.7+
- FFmpeg (for video processing)
- Google Gemini API key
- Internet connection for model downloads

## Installation

1. **Clone the repository**
   ```bash
   git clone git@github.com:auspicious27/Video-timestamp-transcribe.git
   cd Video-timestamp-transcribe
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install FFmpeg**
   - **macOS**: `brew install ffmpeg`
   - **Ubuntu/Debian**: `sudo apt update && sudo apt install ffmpeg`
   - **Windows**: Download from [FFmpeg website](https://ffmpeg.org/download.html)

4. **Set up Google Gemini API**
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Replace the API key in `timestamp.py` line 8

## Usage

### Basic Transcription (`Transcribecode.py`)

For simple video/audio to text conversion:

```python
# Edit the file_path variable in Transcribecode.py
file_path = "your_video.mp4"

# Run the script
python Transcribecode.py
```

### Advanced Timestamp Summarization (`timestamp.py`)

For detailed timestamp-based analysis:

```python
# Edit the video_path variable in timestamp.py
video_path = "your_video.mp4"

# Run the script
python timestamp.py
```

## Configuration

### API Keys
- **Google Gemini**: Update the `API_KEY` variable in `timestamp.py`
- **Whisper**: No API key required (runs locally)

### Model Settings
- **Whisper Model**: Change `"base"` to `"tiny"`, `"small"`, `"medium"`, or `"large"` for different accuracy/speed trade-offs
- **Chunk Length**: Modify `chunk_length=20*60` in `timestamp.py` to change video chunk duration (default: 20 minutes)

## Output

### Basic Transcription
- Creates a text file with the same name as input file + "_transcription.txt"
- Outputs transcription to console

### Timestamp Summarization
- Creates `video_summary.txt` with timestamped summaries
- Each chunk includes start time, end time, and AI-generated summary

## Example Output

```
Chunk 1 (0:00:00 - 0:20:00):
• Introduction to the topic
• Key concepts explained
• Initial examples provided

Chunk 2 (0:20:00 - 0:40:00):
• Advanced techniques discussed
• Practical applications shown
• Q&A session begins
```

## Requirements

Create a `requirements.txt` file with:

```
whisper
moviepy
transformers
google-generativeai
torch
```

## Troubleshooting

1. **FFmpeg not found**: Ensure FFmpeg is installed and in your system PATH
2. **CUDA errors**: Install PyTorch with CUDA support if using GPU
3. **Memory issues**: Use smaller Whisper models or reduce chunk size
4. **API key errors**: Verify your Google Gemini API key is correct and has sufficient quota

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- OpenAI for Whisper ASR
- Google for Gemini AI
- MoviePy for video processing
- Transformers library for model loading
