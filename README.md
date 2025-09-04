# 🕵️‍♂️ SpyPop_2.0 Media – Secret Message, Image & Audio Popup with Self-Destruct
SpyPop Media is the extended version of my original SpyPop project.
While the classic SpyPop only supported secret text messages, this upgraded version can now handle Text, Images, and Audio messages – all wrapped in a dramatic spy-style popup with a self-destruct countdown.

This project is for educational and demonstration purposes only. It ensures privacy for temporary sensitive information and securely removes all traces after viewing.

## ✨ Features

- 🔐 Encrypt & Decrypt
  - main_media.py – Encrypts text, images, or audio files.
  - secret_media.py – Decrypts and shows/plays the content in a popup.
- 🖼 Supports Multiple Modes
  - Secret Text messages (shown in styled popup).
  - Secret Images (auto-scaled to fit window).
  - Secret Audio (plays .wav or .mp3 files).
- ⏳ Countdown Timer
  - Shows a clear countdown before destruction.
- 💥 Self-Destruct Mechanism
  - Deletes secret.enc, secret.key, secret.type.
  - Deletes decrypted temp files (temp_image, temp_audio.wav/.mp3).
  - Deletes itself (secret_media.py / .exe).
- 🔑 Owner Override
  - Type 007 to cancel self-destruct (for testing/debugging).
- ❌ No Internet Access
  - Does NOT upload, share, or send any data externally.
  - Only touches its own project-related files.

## 📂 File Structure

    SpyPop/
    │── main.py             # Original SpyPop (text only)
    │── secret.py           # Original SpyPop popup
    │── main_media.py       # Extended version – encryption for text/image/audio
    │── secret_media.py     # Extended popup – decryption & display/play
    │── demo.png            # (Optional) demo screenshot

## 🚀 How to Use

### Step 1: Encrypt a Secret

- Run main_media.py
``` python main_media.py
```
- Choose:
  - 1.Text → type your secret message.
  - 2.Image → provide a .png/.jpg file.
  - 3.Audio → provide a .wav/.mp3 file.
- It will generate:
  - secret.enc → Encrypted data
  - secret.key → Encryption key
  - secret.type → Type metadata (text, image, audio)

### 🔹 Step 2: Share Securely

- Send the recipient:
  - secret.enc
  - secret.key
  - secret_media.py (or compiled secret_media.exe)

### 🔹 Step 3: View Secret (Popup)

- Recipient runs:
```python secret_media.py
```
  - Popup opens showing message / image / audio.
  - Countdown starts.
  - After countdown → all files + executable self-destruct.

## ⚠️ Antivirus / Defender Notice

- The self-deletion feature may trigger false positives in some antivirus software.
- The code is 100% open-source and inspectable.
- Review before running if unsure.


## 🛠 Building .exe

- You can convert secret_media.py into .exe using PyInstaller:
```pip install pyinstaller
```
```pyinstaller --onefile --noconsole secret_media.py
```

- Output will be in the dist/ folder as secret_media.exe.
- Add --icon=icon.ico for a custom icon


## 🎥 Demo


## ⚖️ Disclaimer

- This project is created for educational purposes only.
- It does NOT harm personal files, does NOT access system directories, and does NOT send data over the internet.
- Use responsibly — once run, the secret will self-destruct and is irreversible.

## 📄 License

This project is licensed under the MIT License

| Feature                   | 📝 Original SpyPop | 🎬 SpyPop Media (Extended)    |
| ------------------------- | ------------------ | ----------------------------- |
| Secret Text Message       | ✅ Supported        | ✅ Supported                   |
| Secret Images             | ❌ Not Supported    | ✅ Supported                   |
| Secret Audio              | ❌ Not Supported    | ✅ Supported (`.wav` / `.mp3`) |
| Countdown Self-Destruct   | ✅ Yes              | ✅ Improved                    |
| Owner Override (`007`)    | ✅ Yes              | ✅ Yes                         |
| Self-Deleting Executable  | ✅ Yes              | ✅ Yes                         |
| Antivirus False Positives | ⚠️ Possible        | ⚠️ Possible                   |
| Educational Purpose       | ✅ Yes              | ✅ Yes                         |















