lukuja = [48, 53, 71, 38, 28, 79, 46, 94, 24, 36, 78, 26, 20, 73, 72, 2, 26, 25, 75, 53, 56, 87, 7, 58, 25, 36, 40, 43, 71, 49, 55, 16, 79, 80, 30, 15, 9, 83, 80, 79, 75, 52, 43, 6, 48, 65, 48, 90, 6, 69, 57, 1, 55, 77, 93, 10, 19, 20, 46, 9, 35, 67, 1, 9, 31, 80, 37, 72, 79, 25, 9, 38, 38, 11, 62, 64, 82, 39, 68, 70, 21, 12, 7, 46, 16, 3, 8, 12, 56, 92, 26, 91, 25, 39, 49, 95, 29, 83, 87, 94]


# Lasketaan keskiarvo listasta "lukuja" eri tavoin

# Listaa on mahdollista käsitellä (tarpeettoman monimutkaisesti)
# esimerkiksi while-silmukassaa
sum_a_lukuja = 0
count_a_lukuja = 0
while count_a_lukuja < len(lukuja):
    sum_a_lukuja += lukuja[count_a_lukuja]
    count_a_lukuja += 1
print(f"Lukujen keskiarvo on: {sum_a_lukuja / count_a_lukuja}")


# On myös mahdollista käyttää range() funktiota ja for-silmukkaa
# järjestysnumeroiden iterointiin
sum_b_lukuja = 0
count_b_lukuja = 0
for i in range(0, len(lukuja)):
    sum_b_lukuja += lukuja[i]
    count_b_lukuja += 1
print(f"Lukujen keskiarvo on: {sum_b_lukuja / count_b_lukuja}")


# in-avainsanalla on mahdollista osoittaa in-sanan vasemmanpuoliseen
# muuttujaan jokainen iteroitavan muuttujan (esim. lista) arvo vuorollaan
# ja ajaa sillee sen jälkeen silmukan sisältämä koodi. Tämä tekee toteutuksesta
# siistimmän näköisen.
sum_c_lukuja = 0
count_c_lukuja = 0
for luku in lukuja:
    sum_c_lukuja += luku
    count_c_lukuja += 1
print(f"Lukujen keskiarvo on: {sum_c_lukuja / count_c_lukuja}")


# Keskiarvon laskemiseen voi hyödyntää myös Pythonin sisäänrakennettuja ominaisuuksia.
print(f"Lukujen keskiarvo on: {sum(lukuja) / len(lukuja)}")


# Myös sanakirjan iterointi on mahdollista, mutta iterointiin on useita
# erilaisia tapoja. Siitä mitä tietoa iteroidaan, riippuu siitä, millä
# funktiolla iterointi käynnistetään.
print("")
sanakirja_1 = {
    "avain_1": "arvo_1",
    "avain_2": "arvo_2",
    "avain_3": "arvo_3",
    "avain_4": "arvo_4",
    "avain_5": "arvo_5",
    "avain_6": "arvo_6",
    "avain_7": "arvo_7",
    "avain_8": "arvo_8",
    "avain_9": "arvo_9",
}
# Seuraavat kolme esimerkkiä ovat loogisesti yhtäläisiä tapoja iteroida
# sanakirjaa

# Tavallinen for x in y iterointi antaa muuttujan x arvoksi sanakirjan y
# jokaisen avaimen vuorollaan
for key in sanakirja_1:
    print(f"Avaimen {key} arvo on {sanakirja_1[key]}")
print("")
# Iteroitaessa .items()-metodilla saadaan puolestaan lista monikkoja,
# jotka vastaavat sanakirjan avain-arvo -pareja.
for item in sanakirja_1.items():
    print(f"Avaimen {item[0]} arvo on {item[1]}")
print("")
# Monikko on mahdollista avata erillisiin muuttujiin, jolloin muuttujien
# järjestys vastaa monikon järjestystä. Tässä esimerkissä muuttuja key
# saa arvokseen items()-listan monikkojen ensimmäiset arvot vuorollaan
# (eli sanakirjan avaimet), value-muuttuja puolestaan saa avaimen takana
# majailevan arvon
for key, value in sanakirja_1.items():
    print(f"Avaimen {key} arvo on {value}")
