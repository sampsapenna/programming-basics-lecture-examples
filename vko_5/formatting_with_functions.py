"""Example with functions from the week 3 formatting homework."""


import random
import datetime


MUNICIPALITIES = ['Akaa', 'Alajärvi', 'Alavieska', 'Alavus', 'Asikkala', 'Askola', 'Aura', 'Brändö', 'Eckerö', 'Enonkoski', 'Enontekiö', 'Espoo', 'Eura', 'Eurajoki', 'Evijärvi', 'Finström', 'Forssa', 'Föglö', 'Geta', 'Haapajärvi', 'Haapavesi', 'Hailuoto', 'Halsua', 'Hamina', 'Hammarland', 'Hankasalmi', 'Hanko', 'Harjavalta', 'Hartola', 'Hattula', 'Hausjärvi', 'Heinola', 'Heinävesi', 'Helsinki', 'Hirvensalmi', 'Hollola', 'Huittinen', 'Humppila', 'Hyrynsalmi', 'Hyvinkää', 'Hämeenkyrö', 'Hämeenlinna', 'Ii', 'Iisalmi', 'Iitti', 'Ikaalinen', 'Ilmajoki', 'Ilomantsi', 'Imatra', 'Inari', 'Inkoo', 'Isojoki', 'Isokyrö', 'Janakkala', 'Joensuu', 'Jokioinen', 'Jomala', 'Joroinen', 'Joutsa', 'Juuka', 'Juupajoki', 'Juva', 'Jyväskylä', 'Jämijärvi', 'Jämsä', 'Järvenpää', 'Kaarina', 'Kaavi', 'Kajaani', 'Kalajoki', 'Kangasala', 'Kangasniemi', 'Kankaanpää', 'Kannonkoski', 'Kannus', 'Karijoki', 'Karkkila', 'Karstula', 'Karvia', 'Kaskinen', 'Kauhajoki', 'Kauhava', 'Kauniainen', 'Kaustinen', 'Keitele', 'Kemi', 'Kemijärvi', 'Keminmaa', 'Kemiönsaari', 'Kempele', 'Kerava', 'Keuruu', 'Kihniö', 'Kinnula', 'Kirkkonummi', 'Kitee', 'Kittilä', 'Kiuruvesi', 'Kivijärvi', 'Kokemäki', 'Kokkola', 'Kolari', 'Konnevesi', 'Kontiolahti', 'Korsnäs', 'Koski Tl', 'Kotka', 'Kouvola', 'Kristiinankaupunki', 'Kruunupyy', 'Kuhmo', 'Kuhmoinen', 'Kumlinge', 'Kuopio', 'Kuortane', 'Kurikka', 'Kustavi', 'Kuusamo', 'Kyyjärvi', 'Kärkölä', 'Kärsämäki', 'Kökar', 'Lahti', 'Laihia', 'Laitila', 'Lapinjärvi', 'Lapinlahti', 'Lappajärvi', 'Lappeenranta', 'Lapua', 'Laukaa', 'Lemi', 'Lemland', 'Lempäälä', 'Leppävirta', 'Lestijärvi', 'Lieksa', 'Lieto', 'Liminka', 'Liperi', 'Lohja', 'Loimaa', 'Loppi', 'Loviisa', 'Luhanka', 'Lumijoki', 'Lumparland', 'Luoto', 'Luumäki', 'Maalahti', 'Maarianhamina - Mariehamn', 'Marttila', 'Masku', 'Merijärvi', 'Merikarvia', 'Miehikkälä', 'Mikkeli', 'Muhos', 'Multia', 'Muonio', 'Mustasaari', 'Muurame', 'Mynämäki', 'Myrskylä', 'Mäntsälä', 'Mänttä-Vilppula', 'Mäntyharju', 'Naantali', 'Nakkila', 'Nivala', 'Nokia', 'Nousiainen', 'Nurmes', 'Nurmijärvi', 'Närpiö', 'Orimattila', 'Oripää', 'Orivesi', 'Oulainen', 'Oulu', 'Outokumpu', 'Padasjoki', 'Paimio', 'Paltamo', 'Parainen', 'Parikkala', 'Parkano', 'Pedersören kunta', 'Pelkosenniemi', 'Pello', 'Perho', 'Petäjävesi', 'Pieksämäki', 'Pielavesi', 'Pietarsaari', 'Pihtipudas', 'Pirkkala', 'Polvijärvi', 'Pomarkku', 'Pori', 'Pornainen', 'Porvoo', 'Posio', 'Pudasjärvi', 'Pukkila', 'Punkalaidun', 'Puolanka', 'Puumala', 'Pyhtää', 'Pyhäjoki', 'Pyhäjärvi', 'Pyhäntä', 'Pyhäranta', 'Pälkäne', 'Pöytyä', 'Raahe', 'Raasepori', 'Raisio', 'Rantasalmi', 'Ranua', 'Rauma', 'Rautalampi', 'Rautavaara', 'Rautjärvi', 'Reisjärvi', 'Riihimäki', 'Ristijärvi', 'Rovaniemi', 'Ruokolahti', 'Ruovesi', 'Rusko', 'Rääkkylä', 'Saarijärvi', 'Salla', 'Salo', 'Saltvik', 'Sastamala', 'Sauvo', 'Savitaipale', 'Savonlinna', 'Savukoski', 'Seinäjoki', 'Sievi', 'Siikainen', 'Siikajoki', 'Siikalatva', 'Siilinjärvi', 'Simo', 'Sipoo', 'Siuntio', 'Sodankylä', 'Soini', 'Somero', 'Sonkajärvi', 'Sotkamo', 'Sottunga', 'Sulkava', 'Sund', 'Suomussalmi', 'Suonenjoki', 'Sysmä', 'Säkylä', 'Taipalsaari', 'Taivalkoski', 'Taivassalo', 'Tammela', 'Tampere', 'Tervo', 'Tervola', 'Teuva', 'Tohmajärvi', 'Toholampi', 'Toivakka', 'Tornio', 'Turku', 'Tuusniemi', 'Tuusula', 'Tyrnävä', 'Ulvila', 'Urjala', 'Utajärvi', 'Utsjoki', 'Uurainen', 'Uusikaarlepyy', 'Uusikaupunki', 'Vaala', 'Vaasa', 'Valkeakoski', 'Vantaa', 'Varkaus', 'Vehmaa', 'Vesanto', 'Vesilahti', 'Veteli', 'Vieremä', 'Vihti', 'Viitasaari', 'Vimpeli', 'Virolahti', 'Virrat', 'Vårdö', 'Vöyri', 'Ylitornio', 'Ylivieska', 'Ylöjärvi', 'Ypäjä', 'Ähtäri', 'Äänekoski']
FIRST_NAMES_MEN = ["Juhani", "Olavi", "Tapani", "Johannes", "Antero", "Tapio", "Mikael", "Kalevi", "Pekka", "Matti", "Petteri", "Ilmari", "Matias", "Sakari", "Kristian", "Antti", "Juha", "Heikki", "Timo", "Mikko", "Markus", "Aleksi", "Kari", "Jari", "Oskari", "Jukka", "Petri", "Mika", "Jaakko", "Henrik", "Markku", "Lauri", "Kalervo", "Ville", "Valtteri", "Veikko", "Hannu", "Elias", "Janne", "Marko", "Ari", "Seppo", "Tuomas", "Erkki", "Sami", "Ensio", "Juho", "Onni", "Erik", "Eemeli", "Jani", "Eero", "Samuli", "Oliver", "Eino", "Samuel", "Pentti", "Teemu", "Martti", "Harri", "Viljami", "Emil", "Jorma", "Leo", "Jarmo", "Risto", "Toivo", "Pasi", "Niko", "Veli", "Esa", "Joonas", "Jouni", "Olli", "Arto", "Kalle", "Toni", "Vesa", "Daniel", "Väinö", "Santeri", "Armas", "Alexander", "Pertti", "Johan", "Raimo", "Eetu", "Tomi", "Henri", "Sebastian", "Jouko", "Kimmo", "Esko", "Eemil", "Paavo", "Joni", "Anton", "Tommi", "Otto"]
FIRST_NAMES_WOMEN = ["Maria", "Helena", "Johanna", "Kaarina", "Hannele", "Marjatta", "Kristiina", "Emilia", "Sofia", "Elina", "Liisa", "Maarit", "Susanna", "Tuulikki", "Katariina", "Annikki", "Anna", "Leena", "Marja", "Sinikka"]
FIRST_NAMES = FIRST_NAMES_MEN + FIRST_NAMES_WOMEN
SURNAMES = ["Korhonen", "Virtanen", "Nieminen", "Mäkinen", "Hämäläinen", "Mäkelä", "Laine", "Heikkinen", "Koskinen", "Lehtonen", "Järvinen", "Lehtinen", "Saarinen", "Salminen", "Heinonen", "Heikkilä", "Niemi", "Salonen", "Laitinen", "Turunen", "Kinnunen", "Tuominen", "Savolainen", "Salo", "Rantanen", "Jokinen", "Miettinen", "Mattila", "Karjalainen", "Räsänen", "Ahonen", "Lahtinen", "Pitkänen", "Hiltunen", "Ojala", "Leppänen", "Aaltonen", "Leinonen", "Kallio", "Väisänen", "Anttila", "Mustonen", "Hakala", "Laaksonen", "Manninen", "Koivisto", "Lehto", "Laakso", "Hirvonen", "Toivonen", "Kettunen", "Hartikainen", "Nurmi", "Niskanen", "Aalto", "Partanen", "Peltonen", "Rantala", "Lappalainen", "Pulkkinen", "Niemelä", "Rissanen", "Seppälä", "Saari", "Kauppinen", "Hakkarainen", "Hänninen", "Huttunen", "Seppänen", "Moilanen", "Salmi", "Suominen", "Koskela", "Halonen", "Kemppainen", "Lahti", "Mikkonen", "Peltola", "Parviainen", "Kärkkäinen", "Leskinen", "Ikonen", "Aho", "Ahola", "Koponen", "Pesonen", "Oksanen", "Vainio", "Lindholm", "Heiskanen", "Vuorinen", "Johansson", "Rautiainen", "Mikkola", "Toivanen", "Karppinen", "Nurminen", "Koski", "Immonen", "Honkanen"]


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


def generate_table(n_rows):
    """Generate a table with random data."""
    print(get_table_headers())
    for i in range(1, n_rows + 1):
        print(
            format_table_row(
                i,
                random.choice(FIRST_NAMES),
                random.choice(SURNAMES),
                random.choice(MUNICIPALITIES),
                random.choice(MUNICIPALITIES),
                random.randint(1900, 2026),
                get_random_timestamp(),
            )
        )


def main():
    rows = int(input("Kuinka monta riviä taulukkoa luodaan? (15): ") or "15")

    print("\n\n")
    generate_table(rows)


main()
