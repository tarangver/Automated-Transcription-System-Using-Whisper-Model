# Import Necessary Modules
import os
import time
import whisper
import ffmpeg
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Load Whisper model
# # Change "base" to "small", "medium", or "large" if needed
model = whisper.load_model("large") 

# Define a Function to Transcribe Audio/Video Files
def transcribe_file(file_path):
    """Transcribe an audio/video file and save the transcript."""
    print(f"Processing: {file_path}")

    # Define output transcript file
    output_text_file = file_path + ".txt"

    # Skip already transcribed files
    if os.path.exists(output_text_file):
        print(f"Skipping (Already Transcribed): {file_path}")
        return

    # Convert non-audio files to WAV (if needed)
    audio_path = file_path
    if not file_path.endswith(('.wav', '.mp3', '.aac', '.m4a')):
        audio_path = file_path + ".wav"
        ffmpeg.input(file_path).output(audio_path).run(overwrite_output=True)

    # Transcribe using Whisper
    result = model.transcribe(audio_path)
    transcript = result["text"]

    # Save transcript to a text file
    with open(output_text_file, "w", encoding="utf-8") as f:
        f.write(transcript)

    print(f"✅ Transcription saved: {output_text_file}")

# Implement Recursive Directory Scanning
def scan_directory(directory):
    """Scan directory and transcribe all media files."""
    print(f"🕵🏻 Scanning directory: {directory}")

    # Supported audio/video formats
    supported_formats = ('.mp3', '.wav', '.mp4', '.mkv', '.mov', '.flv', '.aac', '.m4a')

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(supported_formats):
                file_path = os.path.join(root, file)
                transcribe_file(file_path)

# Implement Real-Time Folder Monitoring
class MediaFileHandler(FileSystemEventHandler):
    """Handles new media file events and triggers transcription."""

    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            if file_path.endswith(('.mp3', '.wav', '.mp4', '.mkv', '.mov', '.flv', '.aac', '.m4a')):
                print(f"🆕 New file detected: {file_path}")
                transcribe_file(file_path)
 
# Setup the Watchdog Observer
def monitor_folder(directory):
    """Monitor a folder for new media files."""
    print(f"👩‍💻 Monitoring folder: {directory}")
    event_handler = MediaFileHandler()
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(10)  # Keep script running
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

# Run the Transcription System
if __name__ == "__main__":
    # Change this to your folder path
    target_directory = "D:\CodeHub\MyProject\Machine Learning\Transcription System\media_files"  

    # Step 1: Scan and transcribe existing files
    scan_directory(target_directory)

    # Step 2: Monitor for new files
    monitor_folder(target_directory)
