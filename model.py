import cv2
import numpy as np
import pytesseract
from matplotlib import pyplot as plt


# Function to display an image using matplotlib
def cv2_imshow(image):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Hide axis
    plt.show()


def main(segmented_image_path):

    img = cv2.imread(segmented_image_path)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Get binary-mask
    msk = cv2.inRange(hsv, np.array([0, 0, 175]), np.array([179, 255, 255]))
    krn = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
    dlt = cv2.dilate(msk, krn, iterations=1)
    thr = 255 - cv2.bitwise_and(dlt, msk)

    # OCR
    e= pytesseract.image_to_string(thr,  lang='hrv',config='--psm 10 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ČĆĐŠ')
    e = e.replace("\n", "")
    return e