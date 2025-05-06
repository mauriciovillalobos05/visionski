import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract

img = cv2.imread('placa_q.jpg')

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

height, width = img_rgb.shape[:2]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mask = gray < 30

inverted_mask = (mask.astype(np.uint8)) * 255

blurred = cv2.GaussianBlur(inverted_mask, (15, 15), 0)

subsampled_with_filter = cv2.resize(
    blurred, (width // 8, height // 8), interpolation=cv2.INTER_AREA
)

plt.imshow(subsampled_with_filter, cmap='gray')
plt.title("OCR Input: Black text on white")
plt.axis('off')
plt.show()

text = pytesseract.image_to_string(subsampled_with_filter)

print("OCR Output:")
print(text.strip())
