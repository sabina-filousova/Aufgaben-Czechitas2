import csv
import json

seznam = []

with open("netflix_titles.tsv", encoding="u" \
"tf-8") as soubor:
    radky = soubor.readlines()

hlavicka = radky[0].strip().split('\t')

nazev_idx = hlavicka.index("PRIMARYTITLE")
reziser_idx = hlavicka.index("DIRECTOR")
herci_idx = hlavicka.index("CAST")
zanr_idx = hlavicka.index("GENRES")
rok_idx = hlavicka.index("STARTYEAR")

for radek in radky[1:]:
    radek = radek.strip().split('\t')

    film = {}

    film["title"] = radek[nazev_idx]

    if radek[reziser_idx] != "":
        film["directors"] = radek[reziser_idx].split(", ")
    else:
        film["directors"] = []

    if radek[herci_idx] != "":
        film["cast"] = radek[herci_idx].split(", ")
    else:
        film["cast"] = []

    if radek[zanr_idx] != "":
        film["genres"] = radek[zanr_idx].split(",")
    else:
        film["genres"] = []

    if radek[rok_idx].isdigit():
        rok = int(radek[rok_idx])
        film["decade"] = (rok // 10) * 10
    else:
        continue  

    seznam.append(film)
    

with open("hw02_output.json", "w", encoding="utf-8") as vystup:
    json.dump(seznam, vystup, ensure_ascii=False, indent=4)

print("Hotovo")