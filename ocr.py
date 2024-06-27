import pytesseract
from PIL import Image

def perform_ocr(image: Image) -> str:
    return pytesseract.image_to_string(image)
