#!/usr/bin/env python3
"""Example with functions, formatting, lists and dictionaries."""


import sys
import random
import datetime


# Testidataa, josta esimerkkirivien satunnainen generointi onnistuu.
MUNICIPALITIES = ['Akaa', 'Alajärvi', 'Alavieska', 'Alavus', 'Asikkala', 'Askola', 'Aura', 'Brändö', 'Eckerö', 'Enonkoski', 'Enontekiö', 'Espoo', 'Eura', 'Eurajoki', 'Evijärvi', 'Finström', 'Forssa', 'Föglö', 'Geta', 'Haapajärvi', 'Haapavesi', 'Hailuoto', 'Halsua', 'Hamina', 'Hammarland', 'Hankasalmi', 'Hanko', 'Harjavalta', 'Hartola', 'Hattula', 'Hausjärvi', 'Heinola', 'Heinävesi', 'Helsinki', 'Hirvensalmi', 'Hollola', 'Huittinen', 'Humppila', 'Hyrynsalmi', 'Hyvinkää', 'Hämeenkyrö', 'Hämeenlinna', 'Ii', 'Iisalmi', 'Iitti', 'Ikaalinen', 'Ilmajoki', 'Ilomantsi', 'Imatra', 'Inari', 'Inkoo', 'Isojoki', 'Isokyrö', 'Janakkala', 'Joensuu', 'Jokioinen', 'Jomala', 'Joroinen', 'Joutsa', 'Juuka', 'Juupajoki', 'Juva', 'Jyväskylä', 'Jämijärvi', 'Jämsä', 'Järvenpää', 'Kaarina', 'Kaavi', 'Kajaani', 'Kalajoki', 'Kangasala', 'Kangasniemi', 'Kankaanpää', 'Kannonkoski', 'Kannus', 'Karijoki', 'Karkkila', 'Karstula', 'Karvia', 'Kaskinen', 'Kauhajoki', 'Kauhava', 'Kauniainen', 'Kaustinen', 'Keitele', 'Kemi', 'Kemijärvi', 'Keminmaa', 'Kemiönsaari', 'Kempele', 'Kerava', 'Keuruu', 'Kihniö', 'Kinnula', 'Kirkkonummi', 'Kitee', 'Kittilä', 'Kiuruvesi', 'Kivijärvi', 'Kokemäki', 'Kokkola', 'Kolari', 'Konnevesi', 'Kontiolahti', 'Korsnäs', 'Koski Tl', 'Kotka', 'Kouvola', 'Kristiinankaupunki', 'Kruunupyy', 'Kuhmo', 'Kuhmoinen', 'Kumlinge', 'Kuopio', 'Kuortane', 'Kurikka', 'Kustavi', 'Kuusamo', 'Kyyjärvi', 'Kärkölä', 'Kärsämäki', 'Kökar', 'Lahti', 'Laihia', 'Laitila', 'Lapinjärvi', 'Lapinlahti', 'Lappajärvi', 'Lappeenranta', 'Lapua', 'Laukaa', 'Lemi', 'Lemland', 'Lempäälä', 'Leppävirta', 'Lestijärvi', 'Lieksa', 'Lieto', 'Liminka', 'Liperi', 'Lohja', 'Loimaa', 'Loppi', 'Loviisa', 'Luhanka', 'Lumijoki', 'Lumparland', 'Luoto', 'Luumäki', 'Maalahti', 'Maarianhamina - Mariehamn', 'Marttila', 'Masku', 'Merijärvi', 'Merikarvia', 'Miehikkälä', 'Mikkeli', 'Muhos', 'Multia', 'Muonio', 'Mustasaari', 'Muurame', 'Mynämäki', 'Myrskylä', 'Mäntsälä', 'Mänttä-Vilppula', 'Mäntyharju', 'Naantali', 'Nakkila', 'Nivala', 'Nokia', 'Nousiainen', 'Nurmes', 'Nurmijärvi', 'Närpiö', 'Orimattila', 'Oripää', 'Orivesi', 'Oulainen', 'Oulu', 'Outokumpu', 'Padasjoki', 'Paimio', 'Paltamo', 'Parainen', 'Parikkala', 'Parkano', 'Pedersören kunta', 'Pelkosenniemi', 'Pello', 'Perho', 'Petäjävesi', 'Pieksämäki', 'Pielavesi', 'Pietarsaari', 'Pihtipudas', 'Pirkkala', 'Polvijärvi', 'Pomarkku', 'Pori', 'Pornainen', 'Porvoo', 'Posio', 'Pudasjärvi', 'Pukkila', 'Punkalaidun', 'Puolanka', 'Puumala', 'Pyhtää', 'Pyhäjoki', 'Pyhäjärvi', 'Pyhäntä', 'Pyhäranta', 'Pälkäne', 'Pöytyä', 'Raahe', 'Raasepori', 'Raisio', 'Rantasalmi', 'Ranua', 'Rauma', 'Rautalampi', 'Rautavaara', 'Rautjärvi', 'Reisjärvi', 'Riihimäki', 'Ristijärvi', 'Rovaniemi', 'Ruokolahti', 'Ruovesi', 'Rusko', 'Rääkkylä', 'Saarijärvi', 'Salla', 'Salo', 'Saltvik', 'Sastamala', 'Sauvo', 'Savitaipale', 'Savonlinna', 'Savukoski', 'Seinäjoki', 'Sievi', 'Siikainen', 'Siikajoki', 'Siikalatva', 'Siilinjärvi', 'Simo', 'Sipoo', 'Siuntio', 'Sodankylä', 'Soini', 'Somero', 'Sonkajärvi', 'Sotkamo', 'Sottunga', 'Sulkava', 'Sund', 'Suomussalmi', 'Suonenjoki', 'Sysmä', 'Säkylä', 'Taipalsaari', 'Taivalkoski', 'Taivassalo', 'Tammela', 'Tampere', 'Tervo', 'Tervola', 'Teuva', 'Tohmajärvi', 'Toholampi', 'Toivakka', 'Tornio', 'Turku', 'Tuusniemi', 'Tuusula', 'Tyrnävä', 'Ulvila', 'Urjala', 'Utajärvi', 'Utsjoki', 'Uurainen', 'Uusikaarlepyy', 'Uusikaupunki', 'Vaala', 'Vaasa', 'Valkeakoski', 'Vantaa', 'Varkaus', 'Vehmaa', 'Vesanto', 'Vesilahti', 'Veteli', 'Vieremä', 'Vihti', 'Viitasaari', 'Vimpeli', 'Virolahti', 'Virrat', 'Vårdö', 'Vöyri', 'Ylitornio', 'Ylivieska', 'Ylöjärvi', 'Ypäjä', 'Ähtäri', 'Äänekoski']
FIRST_NAMES_MEN = ["Juhani", "Olavi", "Tapani", "Johannes", "Antero", "Tapio", "Mikael", "Kalevi", "Pekka", "Matti", "Petteri", "Ilmari", "Matias", "Sakari", "Kristian", "Antti", "Juha", "Heikki", "Timo", "Mikko", "Markus", "Aleksi", "Kari", "Jari", "Oskari", "Jukka", "Petri", "Mika", "Jaakko", "Henrik", "Markku", "Lauri", "Kalervo", "Ville", "Valtteri", "Veikko", "Hannu", "Elias", "Janne", "Marko", "Ari", "Seppo", "Tuomas", "Erkki", "Sami", "Ensio", "Juho", "Onni", "Erik", "Eemeli", "Jani", "Eero", "Samuli", "Oliver", "Eino", "Samuel", "Pentti", "Teemu", "Martti", "Harri", "Viljami", "Emil", "Jorma", "Leo", "Jarmo", "Risto", "Toivo", "Pasi", "Niko", "Veli", "Esa", "Joonas", "Jouni", "Olli", "Arto", "Kalle", "Toni", "Vesa", "Daniel", "Väinö", "Santeri", "Armas", "Alexander", "Pertti", "Johan", "Raimo", "Eetu", "Tomi", "Henri", "Sebastian", "Jouko", "Kimmo", "Esko", "Eemil", "Paavo", "Joni", "Anton", "Tommi", "Otto"]
FIRST_NAMES_WOMEN = ["Maria", "Helena", "Johanna", "Kaarina", "Hannele", "Marjatta", "Kristiina", "Emilia", "Sofia", "Elina", "Liisa", "Maarit", "Susanna", "Tuulikki", "Katariina", "Annikki", "Anna", "Leena", "Marja", "Sinikka"]
FIRST_NAMES = FIRST_NAMES_MEN + FIRST_NAMES_WOMEN
LAST_NAMES = ["Korhonen", "Virtanen", "Nieminen", "Mäkinen", "Hämäläinen", "Mäkelä", "Laine", "Heikkinen", "Koskinen", "Lehtonen", "Järvinen", "Lehtinen", "Saarinen", "Salminen", "Heinonen", "Heikkilä", "Niemi", "Salonen", "Laitinen", "Turunen", "Kinnunen", "Tuominen", "Savolainen", "Salo", "Rantanen", "Jokinen", "Miettinen", "Mattila", "Karjalainen", "Räsänen", "Ahonen", "Lahtinen", "Pitkänen", "Hiltunen", "Ojala", "Leppänen", "Aaltonen", "Leinonen", "Kallio", "Väisänen", "Anttila", "Mustonen", "Hakala", "Laaksonen", "Manninen", "Koivisto", "Lehto", "Laakso", "Hirvonen", "Toivonen", "Kettunen", "Hartikainen", "Nurmi", "Niskanen", "Aalto", "Partanen", "Peltonen", "Rantala", "Lappalainen", "Pulkkinen", "Niemelä", "Rissanen", "Seppälä", "Saari", "Kauppinen", "Hakkarainen", "Hänninen", "Huttunen", "Seppänen", "Moilanen", "Salmi", "Suominen", "Koskela", "Halonen", "Kemppainen", "Lahti", "Mikkonen", "Peltola", "Parviainen", "Kärkkäinen", "Leskinen", "Ikonen", "Aho", "Ahola", "Koponen", "Pesonen", "Oksanen", "Vainio", "Lindholm", "Heiskanen", "Vuorinen", "Johansson", "Rautiainen", "Mikkola", "Toivanen", "Karppinen", "Nurminen", "Koski", "Immonen", "Honkanen"]


def get_random_timestamp():
    """Return a random timestamp"""
    date = datetime.datetime(
        random.randint(1984, 2026),
        random.randint(1, 12),
        random.randint(1, 28),
        random.randint(0, 23),
        random.randint(0, 59),
        random.randint(0, 59),
    )
    return f"{date}"


def get_table_headers():
    """Return the table headers."""
    return "{0:>8.8s} {1:>10.10s} {2:>15.15s} {3:>15.15s} {4:>15.15s} {5:>15.15s} {6:>20.20s}".format(
        "Rivi",
        "Etunimi",
        "Sukunimi",
        "Synnyinpaikka",
        "Asuinpaikka",
        "Syntymävuosi",
        "Lisätty"
    )


def format_table_row(index, first_name, last_name, place_of_birth, current_place_of_residence, birth_year, time_of_addition):
    """Return a formatted table row."""
    return (
        f"{index:>8d} {first_name:>10.10s} {last_name:>15.15s} "
        f"{place_of_birth:>15.15s} {current_place_of_residence:>15.15s} "
        f"{birth_year:>15d} {time_of_addition:>20.20s}"
    )


# Mock database schema
# {
#     "first_name": str
#     "last_name": str
#     "place_of_birth": str
#     "current_place_of_residence": str
#     "birth_year": int
#     "time_of_addition": str
# }
# Taulun rivien organisointi sanakirjoiksi mahdollistaa datan tehokkaan
# koneellisen käsittelyn.
def generate_db_row():
    """Generate a row in the hypothetical database."""
    new_row = {
        "first_name": random.choice(FIRST_NAMES),
        "last_name": random.choice(LAST_NAMES),
        "place_of_birth": random.choice(MUNICIPALITIES),
        "current_place_of_residence": random.choice(MUNICIPALITIES),
        "birth_year": random.randint(1900, 2026),
        "time_of_addition": get_random_timestamp(),
    }
    return new_row


def generate_db(n_rows):
    """Generate a hypothetical database with personal information."""
    ret_db = []
    for _ in range(0, n_rows):
        ret_db.append(generate_db_row())

    return ret_db


def generate_and_print_table(db):
    """Generate a table with random data."""
    ret_table = []

    ret_table.append(get_table_headers())

    for row in db:
        new_table_row = format_table_row(
            db.index(row) + 1,
            row["first_name"],
            row["last_name"],
            row["place_of_birth"],
            row["current_place_of_residence"],
            row["birth_year"],
            row["time_of_addition"],
        )
        ret_table.append(new_table_row)

    for row in ret_table:
        print(row)


# Esimerkkiohjelma, joka hyödyntää sanakirjoihin ja listoihin tallennettua dataa
# taulukossa
def use_table_data(n: int = 10000):
    # Luodaan "tietokanta" muuttujaan db. Luodaan tietokantaan myös 10 000 riviä
    # synteettistä dataa, ja demonstroidaan datan käyttöä.

    db = generate_db(n)

    # Tietokannan rivien määrä on mahdollista tarkistaa sisäänrakennetulla funktiolla
    # len()
    print(f"Tietokannan rivien määrä {len(db)}")
    # Koska tietokanta on nyt tallennettu listaan, on mahdollista lisätä uusia rivejä
    # helposti. Lisätään esimerkkinä uudet 100 riviä dataa tietokantaan.
    for _ in range(0, 100):
        db.append(generate_db_row())
    print(f"Tietokannan rivien määrä on lisäysten jälkeen {len(db)}")

    # Koneluettavassa muodossa oleva tietokanta mahdollistaa meille tehokkaan datankäsittelyn.
    
    # Voimme esimerkiksi tarkistaa, kuinka moni henkilö tietokannassa on syntynyt
    # vuonna 85. Tämä voidaan tehdä joko tavallisella silmukalla
    born_85 = 0 
    for row in db:
        if row["birth_year"] == 1985:
            born_85 += 1
    print(f"Vuonna 85 syntyneitä on tietokannassa {born_85}.")
    # Tai käyttäen sisäänrakennettuja funktiota len() ja filter(), sekä tyyppimuunnosta list()
    print(f"Vuonna 85 syntyneitä on tietokannassa {
        len(list(filter(lambda row: row['birth_year'] == 1985, db)))
    }.")

    print("")
    # On nyt myös helppoa tulostaa esimerkiksi kaikkien niiden ihmisten nimet, joiden sukunimi
    # on Koski. Tehdään tämä selkeyden vuoksi for-silmukalla.
    last_name_is_koski = []
    for row in db:
        if row["last_name"] == "Koski":
            last_name_is_koski.append(row)
    # Tulostetaan kaikki Kosket näytölle. Koska "generate_and_print_table" ottaa argumenttina
    # listan tietokannan rivejä, mikä tahansa listaus on mahdollista tulostaa suoraan funktiota
    # kutsumalla. Annetaan vain argumentiksi lista tietokannan rivejä.
    if len(last_name_is_koski) < 25:
        print("Tietokannan henkilöt, joiden sukunimi on Koski")
        generate_and_print_table(last_name_is_koski)
    else:
        print(f"Ei tulosteta Koskia, sillä rivejä oli peräti {len(last_name_is_koski)}.")

    # Voimme halutessamme myös järjestää tietokannan listauksen, esimerkiksi em. Kosket
    # syntymävuoden mukaan nousevassa järjestyksessä. Koska tässä käytetään listan omaa
    # metodia, järjestyy muuttujaan tallennettu lista kokonaisuudessaan.
    # Käytämme tässä esimerkissä ns lambda-funktiota, joka mahdollistaa tiiviimmän
    # järjestelyfunktion käyttämisen. Tässä voi käyttää myös tavallista def-avainsanalla
    # määriteltyä funktiota.
    if len(last_name_is_koski) < 25:
        print("Tietokannan henkilöt, joiden sukunimi on Koski, järjesteltynä synnyinvuoden mukaan.")
        last_name_is_koski.sort(key=lambda row: row["birth_year"])
        generate_and_print_table(last_name_is_koski)
    else:
        print(f"Ei tulosteta Koskia vieläkään, sillä rivejä oli edelleen {len(last_name_is_koski)}")

    # Mikäli tiedolla haluaa tehdä enemmänkin operaatioita, voi alkaa miettimään esimerkiki
    # millaisella algoritmilla seuraaviin kysymyksiin on mahdollista vastata.
    #   1. Minkä nimisillä ihmisillä on tietokannassa vähiten kaimoja?
    #   2. Ketkä asuvat edelleen synnyinpaikassaan?
    #   3. Miten tietokannan henkilöt voitaisiin järjestellä asuinpaikan mukaan?
    #      (vihje, luo uusi sanakirja, jonka avaimina toimivat paikkakunnat, ja lajittele
    #       tietokannan rivit sinne paikkakunnan perusteella)
    #   4. Kuinka monta täyskaimaa (sama etunimi ja sukunimi) tietokannassa on?
    #
    # Tässä vielä esimerkkitoteutukset vastauksena näihin kysymyksiin. Toteutus voi hyödyntää
    # myös ominaisuuksia, joita ei ole vielä käsitelty.

    # 1. Minkä nimisillä ihmisillä on vähiten kaimoja? Ts., mikä on tietokannan harvinaisin nimi.
    # Haetaan tietokannan riveistä pelkät nimet
    name_fields_in_db = [row["first_name"] for row in db]
    # Luodaan joukko uniikeista nimistä tietokannassa
    unique_names_in_db = set(name_fields_in_db)
    # Luodaan sanakirja, jossa nimen perusteella on merkattu nimen esiintymiskerrat.
    # Käytetään dict.fromkeys() sanakirjan valmisteluun käyttöä varten.
    names_by_frequency = dict.fromkeys(unique_names_in_db, 0)
    # Nyt kun meillä on sanakirja, jossa nimet toimivat avaimena ja jokaisen avaimen arvoksi
    # on alustettu 0, voimme suorittaa laskennan helposti.
    for name in unique_names_in_db:
        names_by_frequency[name] = name_fields_in_db.count(name)
    # Tämän jälkeen voimme etsiä sanakirjasta nimen, jonka arvo on alhaisin
    rarest_name = ""
    # Alustetaan lukumäärä korkealle, ettei rikota vertailua silmukassa
    rarest_name_count = len(name_fields_in_db)
    for name, count in names_by_frequency.items():
        if count < rarest_name_count:
            rarest_name = name
            rarest_name_count = count
    # Tämän jälkeen tulostetaan vastaus
    print("")
    print("Tarkistetaan harvinaisin nimi tietokannassa...")
    print(f"Harvinaisin nimi tietokannassa on {rarest_name}, joka esiintyy tietokannassa {rarest_name_count} kertaa.\n")

    # 2. Ketkä asuvat edelleen synnyinpaikkakunnallaan?
    # Luodaan lista riveistä, joilla syynnyin- ja asuinpaikkakunta on sama.
    # Tehdään tämä sisäänrakennetulla funktiolla filter().
    print("Tarkistetaan kuinka moni tietokannan henkilö asuu edelleen synnyinpaikkakunnallaan...")
    same_birth_place_and_place_of_residence = list(
        filter(
            lambda row: row["place_of_birth"] == row["current_place_of_residence"],
            db
        )
    )
    print(f"Yhteensä {len(same_birth_place_and_place_of_residence)} henkilöä asuu synnyinpaikkakunnallaan.\n")

    # 3. Miten tietokannan henkilöt voitaisiin järjestellä asuinpaikan mukaan?
    # Luodaan sanakirja, jossa kunta toimii avaimena, ja arvona toimivat rivit, joissa kyseinen
    # paikkakunta esiintyy nykyisenä asuinkuntana. Käytetään jälleen dict.fromkeys() sanakirjan
    # alustamiseen, ja luodaan avaimiksi joukko uniikeista asuinpaikoista.
    print("Lajitellaan tietokannan henkilöt asuinpaikan mukaan, ja selvitetään yleisin asuinpaikka...")
    places_of_residence = [row["current_place_of_residence"] for row in db]
    unique_places_of_residence = set(places_of_residence)
    # Luodaan sanakirja, jossa asuinpaikat toimivat avaimina, ja arvot ovat listoja riveistä
    rows_by_place_of_residence = dict.fromkeys(unique_places_of_residence, [])
    # Iteroidaan tietokannan rivit ja lajitellaan ne tietokantaan asuinpaikan perusteella
    for row in db:
        rows_by_place_of_residence[row["current_place_of_residence"]].append(row)
    # Tämän jälkeen on mahdollista esimerkiksi hakea paikkakunta, jossa asuu eniten tietokannassa
    # esiintyviä henkilöitä
    most_popular_place_of_residence = ""
    most_popular_place_of_residence_count = 0
    for place in rows_by_place_of_residence:
        count = len(rows_by_place_of_residence[place])
        if count > most_popular_place_of_residence_count:
            most_popular_place_of_residence = place
            most_popular_place_of_residence_count = count
    print(f"Yleisin asuinpaikka on {most_popular_place_of_residence}, jossa asuu {most_popular_place_of_residence_count} tietokannan henkilöä.\n")

    # 4. Kuinka monta täyskaimaa (sama etunimi ja sukunimi) tietokannassa on?
    # Tämä onkin jo vaikeampi tapaus, tarpeen on löytää kaikki tietokannassa esiintyvät
    # etunimi+sukunimi -yhdistelmät, ja laskea niiden esiintyvyys. Tässä kohtaa lienee
    # helpointa luoda tyhjä sanakirja, jossa avaimena toimivat etunimi+sukunimi yhdistelmät,
    # ja alkaa täydentää sitä aina uuden yhdistelmän löytyessä. Kas näin:
    print("Etsitään kenellä tietokannassa on eniten täyskaimoja.")
    people_by_full_name = {}
    for row in db:
        # Tarkistetaan esiintyykö täysi nimi jo tietokannassa. Mikäli ei, lisätään se sinne.
        full_name = f"{row['first_name']} {row['last_name']}"
        # Onko nimi jo sanakirjassa?
        if full_name in people_by_full_name:
            # Lisää yksi täyskaima lisää sanakirjaan
            people_by_full_name[full_name] += 1
        # Muutoin, alustetaan sanakirjan avain arvoon 1, sillä löydettiin ensimmäinen esiintyminen
        else:
            people_by_full_name[full_name] = 1
    # Lopuksi voidaan etsiä jälleen sanakirjasta yleisin yhdistelmä
    most_popular_full_name = ""
    most_popular_full_name_count = 0
    for full_name, count in people_by_full_name.items():
        if count > most_popular_full_name_count:
            most_popular_full_name = full_name
            most_popular_full_name_count = count
    if most_popular_full_name_count == 1:
        print("Kellään tietokannassa ei ole täyskaimoja!")
    else:
        print(f"Yleisin täyskaima oli {most_popular_full_name}, joka esiintyi {most_popular_full_name_count} kertaa.")


def main():
    """Main program."""
    # Lisätään mahdollisuus antaa ohjelmalle argumenttina tietokannan koko
    db_size: int = 0
    try:
        # sys.argv mahdollistaa meille komentoriviargumenttien lukemisen listalta
        db_size = int(sys.argv[1])
    except Exception:
        try:
            # Mikäli moduuli suoritetaan sellaisenaan, argumentteja on kahden sijasta
            # vain yksi.
            db_size = int(sys.argv[0])
        except Exception:
            db_size = 10000

    print(f"Generoidaan tietokanta {db_size:d} rivillä.")
    input("Paina enter jatkaaksesi...")

    use_table_data(db_size)


# Suorita pääohjelma main() mikäli moduuli ajetaan pääohjelmana
if __name__ == "__main__":
    main()
