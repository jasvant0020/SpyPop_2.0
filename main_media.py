from cryptography.fernet import Fernet
import os

def save_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def encrypt_data(data: bytes, key: bytes):
    cipher = Fernet(key)
    return cipher.encrypt(data)

def encrypt_text():
    msg = input("🔐 Enter your secret message: ").encode()
    return msg, "text"

def encrypt_file(choice):
    if choice == "2":
        file_path = input("📂 Enter image file path (.png/.jpg/.jpeg): ").strip()
        valid_ext = [".png", ".jpg", ".jpeg"]
        ftype = "image"
    else:  # choice == "3"
        file_path = input("🎵 Enter audio file path (.wav/.mp3): ").strip()
        valid_ext = [".wav", ".mp3"]
        ftype = "audio"

    if not os.path.exists(file_path):
        raise FileNotFoundError("File not found!")

    ext = os.path.splitext(file_path)[1].lower()
    if ext not in valid_ext:
        raise ValueError(f"Invalid file type for {ftype}: {ext}")

    with open(file_path, "rb") as f:
        data = f.read()

    return data, ftype

if __name__ == "__main__":
    print("Choose type:")
    print("1. Text\n2. Image\n3. Audio")
    choice = input("👉 Enter choice: ").strip()

    if choice == "1":
        raw_data, ftype = encrypt_text()
    elif choice in ["2", "3"]:
        raw_data, ftype = encrypt_file(choice)
    else:
        raise ValueError("❌ Invalid choice! Please enter 1, 2, or 3.")

    key = save_key()
    encrypted = encrypt_data(raw_data, key)

    with open("secret.enc", "wb") as ef:
        ef.write(encrypted)

    with open("secret.type", "w") as tf:
        tf.write(ftype)

    print(f"\n✅ Encrypted {ftype} saved as 'secret.enc' with key in 'secret.key'")
