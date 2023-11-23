from flask import Flask, request, jsonify
from PIL import Image
import pytesseract

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr_process():
    if request.method == 'POST':
        image_file = request.files['image']
        image_data = Image.open(image_file)

        # Perform OCR using PyTesseract
        text = pytesseract.image_to_string(image_data)

        response = {
            'status': 'success',
            'text': text
        }

        return jsonify(response)