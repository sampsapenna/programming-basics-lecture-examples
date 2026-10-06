lista_1 = [10, 11, 12, 13, 14, 15, 16]
lista_2 = ["abd", "bde", "def", "efg"]


# Listan arvojen käsittely

# Listan arvon voi lukea järjestysnumerolla (index),
# joka lisätään litan nimen perään hakasulkuihin []

# Listan ensimmäinen arvo on järjestysluvulla 0 (ns. zero-indexed)
lista_1[2]
lista_1[5]

# Listoja voi laskea yhteen, jolloin niiden sisältämät arvot
# liitetään toistensa perään.
# Kerto, jako ja vähennyslaskua ei tueta.
lista_1 + lista_2

# Listan arvoja voi muuttaa tallentamalla järjestysnumerolla
# uuden arvon
lista_1[3] = 20
# Mikäli listaan haluaa lisätä uusia arvoja, yksittäisen arvon
# voi lisätä seuraavasti
lista_1.append(30)
# Mikäli halutaan lisätä arvo listan keskelle ylikirjoittamatta toista arvoa,
# voi tämän tehdä metodilla insert. Ensimmäinen argumentti on järjestysnumero,
# jolla arvo lisätään. Jälkimmäinen on lisättävä arvo.
lista_1.insert(8, 31)
# Useampia arvoja puolestaan voi lisätä yhteenlaskuin, tai
# seuraavalla listan metodilla. Huomioi, että metodi muokkaa
# alkuperäistä listaa, jonka metodina sitä kutsutaan.
lista_1.extend(lista_2)


# Seuraavalla metodilla on mahdollista tarkistaa listan elementin järjestysnumero
lista_1.index("abd")
# .count() puolestaan kertoo, kuinka monta kertaa ko. arvo esiintyy listalla
lista_1.count("abd")

# Arvoja on mahdollista poistaa metodeilla pop() ja remove(). pop() ottaa
# argumenttina poistettavan järjestysluvun, tai poistaa argumentin puuttuessa
# listan viimeisen arvon.
lista_1.pop()
# .remove() puolestaan poistaa annetun arvon, mikäli se löytyy listasta.
lista_1.remove("efg")

# Mikäli lista halutaan kopioida toiseen muuttujaan ilman, että alkuperäinen
# lista muuttuu muokatessa kopiota, täytyy siitä tehdä kopio metodilla .copy()
lista_3 = lista_1.copy()

# Viimeisenä, clear() tyhjentää listan.
lista_1.clear()
# Listan voi tyhjentää myös ylikirjoittamalla sen tyhjällä listalla
lista_1 = []


lista_3.remove("abc")
lista_3.remove("bed")
lista_3.remove("def")
# Pythonissa on myös sisäänrakennettuna funktioita yleisimmille listoille
# tehtäville operaatioille.
# sorted() järjestää yksinkertaisen listan
sorted(lista_3)
# Listan voi myös järjestää omalla metodilla
lista_3.sort()
# Tai järjestyksen voi kääntää nurin
lista_3.reverse()
# Samoin listan pituuden ja summan tarkistamiseen on omat komentonsa
len(lista_3)
sum(lista_3)


# On myös mahdollista tarkistaa, löytyykö listalta jokin arvo. Tämä tehdään
# avainsanalla "in"
if 30 in lista_3:
    print("Arvo 30 on listalla lista_3")
