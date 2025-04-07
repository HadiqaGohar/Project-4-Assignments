# import qrcode

# def generate_qr(data, filename="qrcode.png"):
#     qr = qrcode.QRCode(
#         version=1,
#         box_size=10,
#         border=5
#     )
#     qr.add_data(data)
#     qr.make(fit=True)
    
#     img = qr.make_image(fill="black", back_color="white")
#     img.save(filename)
#     print(f"QR Code saved as {filename}")

# # User Input
# text = input("Enter text or URL to generate QR code: ")
# generate_qr(text)


import qrcode
import cv2
from pyzbar.pyzbar import decode
from pathlib import Path

def generate_qr(data: str, filename: str = "qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")

    # Save in the same folder as the script (you can change this path)
    save_path = Path.cwd() / filename
    img.save(save_path)
    print(f"[✅] QR Code generated and saved at: {save_path}")

def decode_qr(image_path: str):
    img = cv2.imread(image_path)
    decoded_objects = decode(img)

    if not decoded_objects:
        print("[❌] No QR code found in the image.")
        return

    for obj in decoded_objects:
        print(f"[🔍] Decoded Data: {obj.data.decode('utf-8')}")

# --- User Interface ---
if __name__ == "__main__":
    print("==== QR Code Generator & Decoder ====")
    choice = input("Do you want to [g]enerate or [d]ecode a QR code? ").lower()

    if choice == 'g':
        text = input("Enter text or URL to generate QR code: ")
        filename = input("Enter filename to save (e.g., mycode.png): ")
        generate_qr(text, filename.strip() or "qrcode.png")

    elif choice == 'd':
        image_path = input("Enter path to QR code image: ")
        decode_qr(image_path.strip())

    else:
        print("[⚠️] Invalid choice. Use 'g' or 'd'.")
