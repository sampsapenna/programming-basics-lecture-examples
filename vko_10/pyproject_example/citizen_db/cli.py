"""Main program for managing the mock citizen_db."""


import os.path

import citizen_db.db


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

    user_database = citizen_db.db.generate_db(n_rows)

    help_str = """\
Saatavilla on seuraavat komennot:
a - lisää rivi tietokantaan
p - tulosta tietokanta
s - tallenna tietokanta
o - avaa tietokanta
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
        elif user_command == "o":
            db_path = str(input("Mistä polusta haluat ladata tietokannan? "))
            # Tarkistetaan, onko tiedosto olemassa
            if not os.path.exists(db_path):
                print(f"Tiedostoa {db_path} ei ole olemassa, kirjoitithan tiedoston nimen oikein?")
                # Continue hyppää nykyisen silmukan suorituskerran yli seuraavaan
                continue
            # Tarkistetaan, onko tietokannassa jo rivejä. Mikäli rivejä on,
            # tarjoa käyttäjälle mahdollisuus ylikirjoittaa nykyinen tietokanta.
            if user_database:
                print(f"Muistiin on jo ladattu tietokanta, jossa on {str(len(user_database)) + (" rivi" if len(user_database) == 1 else " riviä")}.")
                confirm_overwrite = str(input("Haluatko ylikirjoittaa nykyisen tietokannan [y/N]?"))
                if confirm_overwrite.lower() != "y":
                    print("Nykyistä tietokantaa ei ylikirjoiteta.")
                    # Continue hyppää nykyisen silmukan suorituskerran yli seuraavaan
                    continue
            try:
                new_database = citizen_db.db.load_db(db_path)
                # Jos saatiin uusi tietokanta, korvataan edellinen uudella
                if new_database:
                    print(f"Ladattiin tietokanta {db_path}, jossa on {str(len(new_database)) + (" rivi" if len(new_database) == 1 else " riviä")}.")
                    user_database = new_database
            # Jos uuden tietokannan nouto epäonnistui, ei yliajeta vanhaa
            except Exception as e:
                continue
        elif user_command == "s":
            db_path = str(input("Mihin polkuun haluat tallentaa tietokannan? "))
            # Tarkistetaan, onko tiedosto olemassa
            if os.path.exists(db_path):
                confirm_overwrite = str(input(f"Tiedosto {db_path} on jo olemassa, haluatko varmasti ylikirjoittaa sen? [y/N]"))
                if confirm_overwrite.lower() != "y":
                    print("Olemassaolevaa tiedostoa ei ylikirjoiteta.")
                    continue
            # Tarkistetaan, yrittääkö käyttäjä tallentaa tyhjää tietokantaa
            if not user_database:
                print("Tyhjää tietokantaa ei voi tallentaa.")
                continue
            try:
                citizen_db.db.save_db(db_path, user_database)
            except Exception as e:
                print(f"Tietokannan tallennus epäonnistui. Syy: {e}.")
        elif user_command == "p":
            # Use the function to render and print the database as a
            # formatted table
            citizen_db.db.generate_and_print_table(user_database)
        elif user_command == "a":
            citizen_db.db.add_new_db_row(user_database)
        else:
            print(f"Tuntematon komento: {user_command}")
            print(help_str)


if __name__ == "__main__":
    main()
