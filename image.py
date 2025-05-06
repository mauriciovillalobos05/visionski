import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract

# Load the input image from file
img = cv2.imread('placa_q.jpg')

# Convert the image from BGR (OpenCV default) to RGB (for visualization)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Get image dimensions
height, width = img_rgb.shape[:2]

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a binary mask where dark pixels (value < 30) are True
mask = gray < 30

# Convert mask to uint8 format and scale to 0–255 (invert logic for Tesseract)
inverted_mask = (mask.astype(np.uint8)) * 255

# Apply Gaussian blur to smooth out noise
blurred = cv2.GaussianBlur(inverted_mask, (15, 15), 0)

# Downsample the image to reduce detail and improve OCR accuracy
subsampled_with_filter = cv2.resize(
    blurred, (width // 8, height // 8), interpolation=cv2.INTER_AREA
)

# Display the preprocessed image (black text on white) for debugging
plt.imshow(subsampled_with_filter, cmap='gray')
plt.title("OCR Input: Black text on white")
plt.axis('off')
plt.show()

# Perform OCR using Tesseract on the processed image
text = pytesseract.image_to_string(subsampled_with_filter)

# Print the recognized text
print("OCR Output:")
print(text.strip())
