# 📌 Automated Transcription System Using Whisper

## 📝 Overview

This is a Python-based **Automated Transcription System** that utilizes **OpenAI’s Whisper model** to transcribe audio and video files. The system supports **recursive directory scanning** and **real-time monitoring**, automatically transcribing newly added media files.

## 🎯 Features

✅ **Recursive Scanning**: Detects all audio/video files in a directory and its subdirectories. 

✅ **Automated Transcription**: Converts speech from media files into text using **Whisper**. 

✅ **Real-Time Monitoring**: Watches folders for new files and transcribes them instantly. 

✅ **Efficient Processing**: Skips already transcribed files to prevent redundant processing. 

✅ **Supports Multiple Formats**: Works with MP3, WAV, MP4, MKV, MOV, FLV, AAC, and M4A.

---

## 🚀 Installation & Setup

### **1️⃣ Install Prerequisites**

Ensure you have **Python 3.8+** installed. Then, install required dependencies:

```bash
pip install torch torchaudio openai-whisper ffmpeg-python watchdog
```

### **2️⃣ Install & Verify FFmpeg**

#### **Windows**:

- Download from [FFmpeg Official Site](https://ffmpeg.org/download.html) and add to system PATH.

```bash
FFmpeg Official Site > Windows > Windows builds from gyan.dev > ffmpeg-release-full.7z
```

Verify installation:

```bash
ffmpeg -version
```

### **3️⃣ Clone the Repository**

```bash
git clone https://github.com/tarangver/Automated-Transcription-System-Using-Whisper-Model.git
cd Automated-Transcription-System-Using-Whisper-Model
cd transcription-system
```

### **4️⃣ Install Requirements**

```bash
pip install -r reqiurement.txt
```

### **5️⃣ Run the Transcription System**

```bash
python transcription_system.py
```

---

## 🔧 How It Works

### **1️⃣ Scanning Existing Files**

The script scans a given directory for supported **audio/video** files and transcribes them.

### **2️⃣ Transcription Process**

- Uses **OpenAI’s Whisper** model for speech-to-text conversion.
- Saves transcriptions as `.txt` files in the same folder as the media file.

### **3️⃣ Real-Time Monitoring**

- Uses the **Watchdog** library to detect newly added media files.
- Automatically transcribes new files **without manual intervention**.

---

## 📂 Project Structure

```
📂 transcription-system
│── problem.pdf              # Detailed Problem statement
│── transcription_system.py  # Main script for transcription
│── requirements.txt         # List of required dependencies
│── media_files/             # Folder containing media files for transcription
```

---

## 🛠 Configuration

- Set the target directory inside `transcription_system.py`:

```python
target_directory = "media_files"  # Change this to your desired folder path
```

- **Change Whisper Model (Optional)**:

```python
model = whisper.load_model("large")  # Options: tiny, base, small, medium, large
```

---

## 🤖 Future Enhancements

✅ **Multi-threading** for faster transcription.\
✅ **GPU Support** for better performance.\
✅ **Web UI** using Flask or Streamlit.

---

## 🏆 Contributors

👤 TARANG VERMA - [GitHub Profile](https://github.com/tarangver)

---

## 📜 License

This project is **open-source** and available under the **MIT License**.

