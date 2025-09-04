import tkinter as tk
from cryptography.fernet import Fernet
import os, sys, tempfile
import subprocess
from PIL import Image, ImageTk  # ✅ supports JPG/PNG
from playsound import playsound  # ✅ cross-platform audio
import threading

def decrypt_data(enc_data, key):
    return Fernet(key).decrypt(enc_data)

def decrypt_and_show():
    # Load files
    with open("secret.key", "rb") as kf:
        key = kf.read()
    with open("secret.enc", "rb") as ef:
        encrypted = ef.read()
    with open("secret.type", "r") as tf:
        ftype = tf.read().strip()

    data = decrypt_data(encrypted, key)

    root = tk.Tk()
    root.title("💬 Secret Message")
    root.configure(bg="#2e2e2e")
    root.attributes("-topmost", True)
    root.resizable(False, False)

    # --- Override (type "007" to cancel self-destruct) ---
    typed_code = ""
    def on_keypress(event):
        nonlocal typed_code
        typed_code += event.char
        if typed_code.endswith("007"):
            if not getattr(sys, 'frozen', False):  # dev mode
                print("[OWNER OVERRIDE] Self-destruct cancelled.")
            root.destroy()
    root.bind("<Key>", on_keypress)

    # --- Handle forced close ---
    def on_force_close():
        root.destroy()
        self_destruct()
    root.protocol("WM_DELETE_WINDOW", on_force_close)
    root.bind("<Alt-F4>", lambda e: on_force_close())

    # Frame for content
    content_frame = tk.Frame(root, bg="#2e2e2e")
    content_frame.pack(padx=20, pady=20)

    # Default window size
    win_w, win_h = 400, 250

    # --- Message/Image/Audio display ---
    if ftype == "text":
        msg = data.decode()
        tk.Label(content_frame, text=msg, fg="white", bg="#2e2e2e",
                 font=("Segoe UI", 14), wraplength=400,
                 justify="center", padx=20, pady=15).pack()
        win_w, win_h = 450, 200

    elif ftype == "image":
        tmp_img = os.path.join(tempfile.gettempdir(), "temp_image")
        with open(tmp_img, "wb") as f:
            f.write(data)

        # Open with Pillow (supports PNG/JPG/JPEG)
        pil_img = Image.open(tmp_img)

        # Auto-scale to screen size
        screen_w = root.winfo_screenwidth()
        screen_h = root.winfo_screenheight()
        max_w, max_h = screen_w - 200, screen_h - 200

        if pil_img.width > max_w or pil_img.height > max_h:
            pil_img.thumbnail((max_w, max_h))

        img = ImageTk.PhotoImage(pil_img)
        tk.Label(content_frame, image=img, bg="#2e2e2e").pack()
        root.tmp_img = img  # keep reference

        win_w, win_h = pil_img.width + 60, pil_img.height + 120

    elif ftype == "audio":
        # Detect extension from header
        if data[:3] == b"ID3":   # MP3 header
            ext = ".mp3"
        elif data[0:4] == b"RIFF":  # WAV header
            ext = ".wav"
        else:
            ext = ".wav"  # fallback

        tmp_audio = os.path.join(tempfile.gettempdir(), "temp_audio" + ext)
        with open(tmp_audio, "wb") as f:
            f.write(data)

        # ✅ Play audio in background
        threading.Thread(target=lambda: playsound(tmp_audio), daemon=True).start()

        tk.Label(content_frame, text="🎵 Playing Secret Audio...",
                 fg="white", bg="#2e2e2e", font=("Segoe UI", 14), pady=10).pack()
        win_w, win_h = 400, 200

    # --- Countdown ---
    countdown = tk.Label(root, font=("Segoe UI", 18, "bold"),
                         fg="#ff4d4d", bg="#2e2e2e", pady=15)
    countdown.pack(side="bottom")

    def start_timer(sec):
        def tick():
            nonlocal sec
            if sec > 0:
                countdown.config(text=f"⚠️ Self-destruct in {sec} sec...")
                sec -= 1
                root.after(1000, tick)
            else:
                root.destroy()
                self_destruct()
        tick()
    start_timer(20)

    # Apply window size
    root.geometry(f"{win_w}x{win_h}")
    root.mainloop()

def self_destruct():
    files_to_delete = [
        "secret.enc", "secret.key", "secret.type",
        "secret_media.py", "secret_media.exe"
    ]

    tmp_img = os.path.join(tempfile.gettempdir(), "temp_image")
    # Both extensions possible for audio
    for ext in [".mp3", ".wav"]:
        files_to_delete.append(os.path.join(tempfile.gettempdir(), "temp_audio" + ext))

    for file in files_to_delete:
        if os.path.exists(file):
            try:
                os.remove(file)
            except:
                pass

    for folder in ["build", "dist", "__pycache__"]:
        if os.path.exists(folder):
            try:
                os.system(f'rmdir /s /q "{folder}"')
            except:
                pass

    if getattr(sys, 'frozen', False):
        exe_path = sys.executable
        bat_path = os.path.join(tempfile.gettempdir(), "killme.bat")
        with open(bat_path, "w") as bf:
            bf.write(f"""@echo off
timeout /t 2 >nul
del "{exe_path}" >nul
del "%~f0" >nul
""")
        os.startfile(bat_path)
    else:
        try:
            os.remove(__file__)
        except:
            pass

# 🚀 Entry point
if __name__ == "__main__":
    decrypt_and_show()
