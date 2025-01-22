Projekt se sastoji od 3 faze:
- **Faza 1**: Učitavanje i priprema podataka (`data_preparation.ipynb`)
- **Faza 2**: Izgradnja modela (`model.ipynb` i `model.py`)
- **Faza 3**: Evaluacija modela (`evaluate_model.ipynb` i `evaluate.ipynb`)

Datoteka `obrada_slika.py` sadrži eksperimentalne funkcije za obradu slika koje su se koristile pri 
izradi projekta, ali naknadno nisu korištene u finalnoj verziji. S obzirom da je u sklopu projekta
problem prepoznavanja i isčitavanja znakova sa registracijske pločice podijeljen na različite faze,
evaluacija modela se odvija samo nad zadnjom fazom, tj. nad prepoznavanjem znakova. Evaluacija nad
ostalim fazama se može provesti ručno i vizualno koristeći funkcije iz datoteke `data_preparation.ipynb`
ili `obrada_slika.py`.
