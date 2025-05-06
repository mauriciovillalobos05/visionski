OCR Plate Reader

This project uses Python to extract text from an image of a license plate using computer vision and OCR. It relies on OpenCV for image processing and pytesseract for text recognition.

How it works:

The image is loaded and converted to RGB and grayscale formats.
A mask is created to isolate dark regions (black text).
The mask is inverted and blurred to reduce noise.
The processed image is downsampled to simplify the input for OCR.
Pytesseract reads the text from the cleaned image.
The result is printed to the console and shown visually using matplotlib.
Dependencies:

Python 3
opencv-python
numpy
matplotlib
pytesseract
Tesseract OCR engine (external dependency)
Install the required Python libraries:

pip install opencv-python numpy matplotlib pytesseract
Install Tesseract OCR:

On Ubuntu:

sudo apt update
sudo apt install tesseract-ocr
On macOS (with Homebrew):

brew install tesseract
On Windows:
Download and install from: https://github.com/tesseract-ocr/tesseract/wiki

Usage:

Place your image as placa_q.jpg in the same folder as the script.
Run the script using Python:
python ocr_plate_reader.py
The processed image will be displayed, and the detected text will be printed.
