#!/usr/bin/env python3
"""Demonstrate a lock file for file operations."""


import datetime
import os
import random
import secrets
import sys
import time


def lock_file(path: str) -> bool:
    """Try locking the file."""
    try:
        # Yritetään luoda tiedosto "exclusive"-tilassa, jolloin toisen ohjelman luotua tiedosto aiemmin
        # suoritus estyy. Näin on mahdollista lukita tiedosto ainoastaan aktiivisen ohjelman käyttöä
        # varten.
        with open(f".{path}.lockfile", "xt") as fx:
            fx.write(f"Locked by {sys.argv[0]} with pid {os.getpid()}\n")
            fx.write(f"{path} is locked.\n")
        print(f"Successfully locked file {path} for editing.")
        return True
    # FileExistsError syntyy, mikäli tiedosto on jo olemassa. Tästä tiedetään, että jokin toinen ohjelma
    # yrittää jo muokata tiedostoa.
    except FileExistsError:
        with open(f".{path}.lockfile", "rt") as fr:
            print(fr.readline(), end="")
            print(f"Failed to lock file {path} for editing. Another application is currently editing the file.")

    return False


def unlock_file(path: str):
    """Unlock the file after editing."""
    try:
        # Poistetaan lukitustiedosto, jolloin jokin toinen ohjelma voi muokata tiedostoa myöhemmin.
        os.remove(f".{path}.lockfile")
        print(f"Freed up file {path} for edits by another instance of this application.")
    except FileNotFoundError:
        pass


def main():
    """Update the requested file safely."""
    # Cache the file path
    try:
        path = sys.argv[1]
    # Mikäli komentoriviargumenttien joukossa ei ole polkua tiedostolle, lopeta ohjelman suoritus.
    except IndexError:
        print("Please provide the file path as an argument.")
        sys.exit(1)

    print(f"Updating file {path} with the new timestamp.")

    # Ohjelma suorittuu jos ja vain jos lukitustiedosto voidaan luoda onnistuneesti
    if lock_file(path):
        # Luodaan muokattavaan tiedostoon todisteita ohjelman suorittumisesta
        with open(path, "at") as f_w:
            # Tallennetaan tiedostoon suorituksen aloitusaika
            f_w.write(f"Process with pid {os.getpid()} started editing file at {datetime.datetime.now().isoformat()}\n")
            f_w.flush()

            # Ohjelma luo kolme satunnaista tunnistetta tiedoston sisään
            for i in range(0, 3):
                time.sleep(random.randint(2, 10))
                f_w.write(f"Process with pid {os.getpid()} generated token {secrets.token_urlsafe(32)} on interation {i}.\n")
                f_w.flush()

            # Tallennetaan tiedostoon suorituksen lopetusaika
            f_w.write(f"Process with pid {os.getpid()} ceased editing file at {datetime.datetime.now().isoformat()}\n")

        # Poistetaan tiedoston lukitus suorituksen päättyessä
        unlock_file(path)
    else:
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
