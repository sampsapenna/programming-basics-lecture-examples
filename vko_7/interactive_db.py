#!/usr/bin/env python3


import random
import time
import datetime


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


def add_new_db_row(user_database):
    """Function to create a new db row from user input."""
    # Pre-fill all required variables to ensure scope visibility outside
    # sub blocks
    first_name = ""
    last_name = ""
    place_of_birth = ""
    place_of_residence = ""
    birth_year = ""

    # Retrieve first name from user
    while True:
        first_name = input("Anna henkilön etunimi: ").strip()
        if first_name.isalpha():
            break
        print(f"Henkilön etunimi sisältää kiellettyjä merkkejä: {first_name}")
        print("Syötä nimi uudelleen käyttäen pelkkiä kirjaimia.")

    # Retrieve last name from user
    while True:
        last_name = input("Anna henkilön sukunimi: ").strip()
        if last_name.isalpha():
            break
        print(f"Henkilön sukunimi sisältää kiellettyjä merkkejä: {last_name}")
        print("Syötä nimi uudelleen käyttäen pelkkiä kirjaimia.")

    # Retrieve city of birth
    while True:
        place_of_birth = input("Anna henkilön synnyinkaupunki: ").strip()
        if place_of_birth.isalpha():
            break
        print(f"Henkilön synnyinkaupunki sisältää kiellettyjä merkkejä: {place_of_birth}")
        print("Syötä synnyinkaupunki uudelleen käyttäen pelkkiä kirjaimia.")

    # Retrieve current place of redicence
    while True:
        place_of_residence = input("Anna henkilön tämänhetkinen asuinpaikka: ").strip()
        if not place_of_residence.isalpha():
            print(f"Henkilön asuinkaupunki sisältää kiellettyjä merkkejä: {place_of_residence}")
            print("Syötä asuinkaupunki uudelleen käyttäen pelkkiä kirjaimia.")
            # Skip to next iteration of the loop
            continue
        place_of_residence = place_of_residence.lower().capitalize()
        # Check if current place of residence is a Finnish municipality
        if place_of_residence not in MUNICIPALITIES:
            print(f"Henkilön asuinkaupunki ei ole Suomen kunta. {place_of_residence}")
            print(f"Syötä Suomen kuntiin kuuluva asuinkaupunki.")
            # Skip to next iteration of the loop
            continue
        break

    # Retrieve birth year
    while True:
        birth_year = input("Anna henkilön synnyinvuosi: ").strip()
        if not birth_year.isdecimal():
            print(f"Synnyinvuosi {birth_year} ei ole oikein kirjoitettu numero.")
            continue
        # Convert birth year to integer
        birth_year = int(birth_year)
        if birth_year > CURRENT_YEAR:
            print("Synnyinvuosi ei voi olla tulevaisuudessa.")
        break

    time_of_addition = f"{datetime.datetime.now()}"

    new_row = {
        "first_name": first_name,
        "last_name": last_name,
        "place_of_birth": place_of_birth,
        "current_place_of_residence": place_of_residence,
        "birth_year": birth_year,
        "time_of_addition": time_of_addition,
    }

    user_database.append(new_row)

    print("Lisättiin seuraavat tiedot tietokantaan:")
    print(format_table_row(len(user_database), first_name, last_name, place_of_birth, place_of_residence, birth_year, time_of_addition))


def main():
    """Main program for the interactive db."""
    # Query user for how many mock rows to generate
    # .strip() to remove unnecessary whitespace
    n_rows = input("Kuinka monta riviä testidataa lisätään tietokantaan? ").strip()
    if n_rows.isdecimal():
        n_rows = int(n_rows)
    else:
        print(f"Syötetty numero {n_rows} ei kelpaa. Käytetään oletusarvoa 10.")
        n_rows = 10

    user_database = generate_db(n_rows)

    help_str = """\
Saatavilla on seuraavat komennot:
a - lisää rivi tietokantaan
p - tulosta tietokanta
q - lopeta ohjelma
h - tulosta tämä teksti
"""

    # Halutessa voidaan toteuttaa uusia komentoja, esimerkiksi haku asuinpaikan mukaan
    # Harjoituksena voi miettiä, miten uusia komentoja (esimerkiksi edellisviiko
    # esimerkeissä käytettyjä) voisi toteuttaa silmukkaan.

    print("Esimerkkiohjelma henkilötietokannan käyttämiseen.")
    print(help_str)
    # main program loop starts here
    while True:
        user_command = input("Minkä komennon haluat suorittaa: ")
        # Parse the user command
        if user_command == "h":
            print(help_str)
        elif user_command == "q":
            print("Lopetetaan ohjelma...")
            return
        elif user_command == "p":
            # Use the function to render and print the database as a
            # formatted table
            generate_and_print_table(user_database)
        elif user_command == "a":
            add_new_db_row(user_database)
        else:
            print(f"Tuntematon komento: {user_command}")
            print(help_str)
















































# Testidataa, josta esimerkkirivien satunnainen generointi onnistuu.
MUNICIPALITIES = ['Akaa', 'Alajärvi', 'Alavieska', 'Alavus', 'Asikkala', 'Askola', 'Aura', 'Brändö', 'Eckerö', 'Enonkoski', 'Enontekiö', 'Espoo', 'Eura', 'Eurajoki', 'Evijärvi', 'Finström', 'Forssa', 'Föglö', 'Geta', 'Haapajärvi', 'Haapavesi', 'Hailuoto', 'Halsua', 'Hamina', 'Hammarland', 'Hankasalmi', 'Hanko', 'Harjavalta', 'Hartola', 'Hattula', 'Hausjärvi', 'Heinola', 'Heinävesi', 'Helsinki', 'Hirvensalmi', 'Hollola', 'Huittinen', 'Humppila', 'Hyrynsalmi', 'Hyvinkää', 'Hämeenkyrö', 'Hämeenlinna', 'Ii', 'Iisalmi', 'Iitti', 'Ikaalinen', 'Ilmajoki', 'Ilomantsi', 'Imatra', 'Inari', 'Inkoo', 'Isojoki', 'Isokyrö', 'Janakkala', 'Joensuu', 'Jokioinen', 'Jomala', 'Joroinen', 'Joutsa', 'Juuka', 'Juupajoki', 'Juva', 'Jyväskylä', 'Jämijärvi', 'Jämsä', 'Järvenpää', 'Kaarina', 'Kaavi', 'Kajaani', 'Kalajoki', 'Kangasala', 'Kangasniemi', 'Kankaanpää', 'Kannonkoski', 'Kannus', 'Karijoki', 'Karkkila', 'Karstula', 'Karvia', 'Kaskinen', 'Kauhajoki', 'Kauhava', 'Kauniainen', 'Kaustinen', 'Keitele', 'Kemi', 'Kemijärvi', 'Keminmaa', 'Kemiönsaari', 'Kempele', 'Kerava', 'Keuruu', 'Kihniö', 'Kinnula', 'Kirkkonummi', 'Kitee', 'Kittilä', 'Kiuruvesi', 'Kivijärvi', 'Kokemäki', 'Kokkola', 'Kolari', 'Konnevesi', 'Kontiolahti', 'Korsnäs', 'Koski Tl', 'Kotka', 'Kouvola', 'Kristiinankaupunki', 'Kruunupyy', 'Kuhmo', 'Kuhmoinen', 'Kumlinge', 'Kuopio', 'Kuortane', 'Kurikka', 'Kustavi', 'Kuusamo', 'Kyyjärvi', 'Kärkölä', 'Kärsämäki', 'Kökar', 'Lahti', 'Laihia', 'Laitila', 'Lapinjärvi', 'Lapinlahti', 'Lappajärvi', 'Lappeenranta', 'Lapua', 'Laukaa', 'Lemi', 'Lemland', 'Lempäälä', 'Leppävirta', 'Lestijärvi', 'Lieksa', 'Lieto', 'Liminka', 'Liperi', 'Lohja', 'Loimaa', 'Loppi', 'Loviisa', 'Luhanka', 'Lumijoki', 'Lumparland', 'Luoto', 'Luumäki', 'Maalahti', 'Maarianhamina - Mariehamn', 'Marttila', 'Masku', 'Merijärvi', 'Merikarvia', 'Miehikkälä', 'Mikkeli', 'Muhos', 'Multia', 'Muonio', 'Mustasaari', 'Muurame', 'Mynämäki', 'Myrskylä', 'Mäntsälä', 'Mänttä-Vilppula', 'Mäntyharju', 'Naantali', 'Nakkila', 'Nivala', 'Nokia', 'Nousiainen', 'Nurmes', 'Nurmijärvi', 'Närpiö', 'Orimattila', 'Oripää', 'Orivesi', 'Oulainen', 'Oulu', 'Outokumpu', 'Padasjoki', 'Paimio', 'Paltamo', 'Parainen', 'Parikkala', 'Parkano', 'Pedersören kunta', 'Pelkosenniemi', 'Pello', 'Perho', 'Petäjävesi', 'Pieksämäki', 'Pielavesi', 'Pietarsaari', 'Pihtipudas', 'Pirkkala', 'Polvijärvi', 'Pomarkku', 'Pori', 'Pornainen', 'Porvoo', 'Posio', 'Pudasjärvi', 'Pukkila', 'Punkalaidun', 'Puolanka', 'Puumala', 'Pyhtää', 'Pyhäjoki', 'Pyhäjärvi', 'Pyhäntä', 'Pyhäranta', 'Pälkäne', 'Pöytyä', 'Raahe', 'Raasepori', 'Raisio', 'Rantasalmi', 'Ranua', 'Rauma', 'Rautalampi', 'Rautavaara', 'Rautjärvi', 'Reisjärvi', 'Riihimäki', 'Ristijärvi', 'Rovaniemi', 'Ruokolahti', 'Ruovesi', 'Rusko', 'Rääkkylä', 'Saarijärvi', 'Salla', 'Salo', 'Saltvik', 'Sastamala', 'Sauvo', 'Savitaipale', 'Savonlinna', 'Savukoski', 'Seinäjoki', 'Sievi', 'Siikainen', 'Siikajoki', 'Siikalatva', 'Siilinjärvi', 'Simo', 'Sipoo', 'Siuntio', 'Sodankylä', 'Soini', 'Somero', 'Sonkajärvi', 'Sotkamo', 'Sottunga', 'Sulkava', 'Sund', 'Suomussalmi', 'Suonenjoki', 'Sysmä', 'Säkylä', 'Taipalsaari', 'Taivalkoski', 'Taivassalo', 'Tammela', 'Tampere', 'Tervo', 'Tervola', 'Teuva', 'Tohmajärvi', 'Toholampi', 'Toivakka', 'Tornio', 'Turku', 'Tuusniemi', 'Tuusula', 'Tyrnävä', 'Ulvila', 'Urjala', 'Utajärvi', 'Utsjoki', 'Uurainen', 'Uusikaarlepyy', 'Uusikaupunki', 'Vaala', 'Vaasa', 'Valkeakoski', 'Vantaa', 'Varkaus', 'Vehmaa', 'Vesanto', 'Vesilahti', 'Veteli', 'Vieremä', 'Vihti', 'Viitasaari', 'Vimpeli', 'Virolahti', 'Virrat', 'Vårdö', 'Vöyri', 'Ylitornio', 'Ylivieska', 'Ylöjärvi', 'Ypäjä', 'Ähtäri', 'Äänekoski']
FIRST_NAMES_MEN = ["Juhani", "Olavi", "Tapani", "Johannes", "Antero", "Tapio", "Mikael", "Kalevi", "Pekka", "Matti", "Petteri", "Ilmari", "Matias", "Sakari", "Kristian", "Antti", "Juha", "Heikki", "Timo", "Mikko", "Markus", "Aleksi", "Kari", "Jari", "Oskari", "Jukka", "Petri", "Mika", "Jaakko", "Henrik", "Markku", "Lauri", "Kalervo", "Ville", "Valtteri", "Veikko", "Hannu", "Elias", "Janne", "Marko", "Ari", "Seppo", "Tuomas", "Erkki", "Sami", "Ensio", "Juho", "Onni", "Erik", "Eemeli", "Jani", "Eero", "Samuli", "Oliver", "Eino", "Samuel", "Pentti", "Teemu", "Martti", "Harri", "Viljami", "Emil", "Jorma", "Leo", "Jarmo", "Risto", "Toivo", "Pasi", "Niko", "Veli", "Esa", "Joonas", "Jouni", "Olli", "Arto", "Kalle", "Toni", "Vesa", "Daniel", "Väinö", "Santeri", "Armas", "Alexander", "Pertti", "Johan", "Raimo", "Eetu", "Tomi", "Henri", "Sebastian", "Jouko", "Kimmo", "Esko", "Eemil", "Paavo", "Joni", "Anton", "Tommi", "Otto"]
FIRST_NAMES_WOMEN = ["Maria", "Helena", "Johanna", "Kaarina", "Hannele", "Marjatta", "Kristiina", "Emilia", "Sofia", "Elina", "Liisa", "Maarit", "Susanna", "Tuulikki", "Katariina", "Annikki", "Anna", "Leena", "Marja", "Sinikka"]
FIRST_NAMES = FIRST_NAMES_MEN + FIRST_NAMES_WOMEN
LAST_NAMES = ["Korhonen", "Virtanen", "Nieminen", "Mäkinen", "Hämäläinen", "Mäkelä", "Laine", "Heikkinen", "Koskinen", "Lehtonen", "Järvinen", "Lehtinen", "Saarinen", "Salminen", "Heinonen", "Heikkilä", "Niemi", "Salonen", "Laitinen", "Turunen", "Kinnunen", "Tuominen", "Savolainen", "Salo", "Rantanen", "Jokinen", "Miettinen", "Mattila", "Karjalainen", "Räsänen", "Ahonen", "Lahtinen", "Pitkänen", "Hiltunen", "Ojala", "Leppänen", "Aaltonen", "Leinonen", "Kallio", "Väisänen", "Anttila", "Mustonen", "Hakala", "Laaksonen", "Manninen", "Koivisto", "Lehto", "Laakso", "Hirvonen", "Toivonen", "Kettunen", "Hartikainen", "Nurmi", "Niskanen", "Aalto", "Partanen", "Peltonen", "Rantala", "Lappalainen", "Pulkkinen", "Niemelä", "Rissanen", "Seppälä", "Saari", "Kauppinen", "Hakkarainen", "Hänninen", "Huttunen", "Seppänen", "Moilanen", "Salmi", "Suominen", "Koskela", "Halonen", "Kemppainen", "Lahti", "Mikkonen", "Peltola", "Parviainen", "Kärkkäinen", "Leskinen", "Ikonen", "Aho", "Ahola", "Koponen", "Pesonen", "Oksanen", "Vainio", "Lindholm", "Heiskanen", "Vuorinen", "Johansson", "Rautiainen", "Mikkola", "Toivanen", "Karppinen", "Nurminen", "Koski", "Immonen", "Honkanen"]

CURRENT_YEAR = 2026

if __name__ == "__main__":
    main()
