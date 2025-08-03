#Sai

import cv2
import pytesseract
import os

image_path = r"./testocr.png"
output_path = r"output.txt"

pytesseract.pytesseract.tesseract_cmd = r"C:\Python_Libraries\tesseract.exe"


def extract_text_from_image(image_path: str) -> str:
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Failed to read image: {image_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text.strip()


def write_text_to_file(text: str, output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)


try:
    extracted = extract_text_from_image(image_path)
    write_text_to_file(extracted, output_path)
    print(f"Text written to: {output_path}")
except Exception as e:
    print(f"Error: {e}")
