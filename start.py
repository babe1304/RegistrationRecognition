import os

import obrada_slika
import model

images = os.listdir('slike_rega')
segment_dir = "temp_output"

for image in images:

    if image.endswith('.png'):
        char_list_len = obrada_slika.main(f'slike_rega/{image}')
        if char_list_len == 0:
            print("Nema segmentiranih karaktera.")
        else:
            print(f"Broj segmentiranih karaktera: {char_list_len}")

        license_plate = ""

        segmenti = os.listdir(segment_dir)
        for i in range(1,char_list_len+1):
            segment = segment_dir + f"/segment{i}.png"
            l = model.main(segment)
            license_plate += l
        print(f"Prepoznata registracija: {license_plate} za sliku {image}.\n")
        license_plate = ""
        # erase all files in segment_dir
        for file in segmenti:
            os.remove(segment_dir + "/" + file)
