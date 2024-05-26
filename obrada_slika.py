import cv2
import numpy as np
import matplotlib.pyplot as plt

# Učitavanje slike
path = "C:/Users/Comp/Desktop/doas/slike_rega/jdndjnddsnj.png"
image = cv2.imread(path)

# Konvertovanje slike u sivi nivo
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Primena Gaussian blur-a
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Primena adaptivnog thresholding-a
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# Definisanje kernel-a za morfološke operacije
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# Primena dilatacije i erozije
dilated = cv2.dilate(thresh, kernel, iterations=1)
eroded = cv2.erode(dilated, kernel, iterations=1)

# Prikazivanje rezultata
plt.imshow(eroded, cmap='gray')
plt.title('Samo slova')
plt.axis('off')
plt.show()
