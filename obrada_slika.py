import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

output_dir = "temp_output"

def segment_characters(image):
    # Kroppovanje slike kako bi se uklonili neželjeni delovi
    cropped_image = image[:, 20:]  # Smanjivanje vrednosti kroppovanja sa leve strane

    # Konvertovanje slike u sivi nivo
    gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

    # Primena Gaussian blur-a
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Ručna binarizacija sa pragom
    _, thresh = cv2.threshold(blurred, 128, 255, cv2.THRESH_BINARY_INV)  # Možete prilagoditi prag 128

    # Prikazivanje binarizovane slike za proveru
    # plt.imshow(thresh, cmap='gray')
    # plt.title('Binarizovana slika')
    # plt.axis('off')
    # plt.show()

    # Definisanje kernel-a za morfološke operacije
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    # Primena dilatacije i erozije
    dilated = cv2.dilate(thresh, kernel, iterations=1)
    eroded = cv2.erode(dilated, kernel, iterations=1)

    # Prikazivanje erodovane i dilatirane slike za proveru
    # plt.imshow(eroded, cmap='gray')
    # plt.title('Erodovana i dilatirana slika')
    # plt.axis('off')
    # plt.show()

    # Pronađi konture
    contours, _ = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Prikazivanje kontura na slici za proveru
    contour_image = cv2.cvtColor(eroded, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)
    # plt.imshow(contour_image)
    # plt.title('Konture na slici')
    # plt.axis('off')
    # plt.show()

    # Filtriraj konture i izdvoji karaktere
    char_list = []
    bounding_boxes = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = w / float(h)
        if 0.2 < aspect_ratio < 1.0 and h > 15:  # Prilagoditi pragove po potrebi
            # Proširi bounding box za 2 piksela na svaku stranu
            x = max(0, x - 3)
            y = max(0, y - 4)
            w = min(eroded.shape[1] - x, w + 6)
            h = min(eroded.shape[0] - y, h + 8)
            
            char = eroded[y:y + h, x:x + w]
            char = cv2.resize(char, (20, 40))
            char_list.append(char)
            bounding_boxes.append((x, y, w, h))

    # Sortiraj karaktere po x koordinati
    char_list = [char for _, char in sorted(zip(bounding_boxes, char_list), key=lambda b: b[0][0])]

    return char_list

def main(path):

    image = cv2.imread(path)
    if image is None:
        print(f"Greška: Slika na putanji {path} nije učitana.")
    else:
        # Prikaz originalne slike
        # plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        # plt.title('Originalna slika')
        # plt.axis('off')
        # plt.show()

        # Segmentacija karaktera
        char_list = segment_characters(image)


        for i, char in enumerate(char_list):
            segment_path = os.path.join(output_dir, f"segment{i+1}.png")
            cv2.imwrite(segment_path, char)

        return len(char_list)

        # fig, axs = plt.subplots(1, len(char_list), figsize=(15, 5))
        # for i, char in enumerate(char_list):
        #     axs[i].imshow(char, cmap='gray')
        #     axs[i].axis('off')
        # plt.show()

if __name__=='__main__':
    print("msj")
    fnames=os.listdir(f'{os.getcwd()}/slike_rega')
    for fname in fnames:
        if fname.endswith('.png'):
            imgpath=f'{os.getcwd()}/slike_rega/{fname}'
            image = cv2.imread(imgpath)
            if image is None:
                print(f"Greška: Slika na putanji {imgpath} nije učitana.")
            else:
                char_list = segment_characters(image)


            for i, char in enumerate(char_list):
                output_dir = f"{os.getcwd()}\segmenti_reg\{fname}"
                if not os.path.exists(output_dir):
                   os.makedirs(output_dir)
                segment_path = os.path.join(output_dir, f"segment{i+1}.png")
                print(segment_path)
                cv2.imwrite(segment_path, char)

            
    