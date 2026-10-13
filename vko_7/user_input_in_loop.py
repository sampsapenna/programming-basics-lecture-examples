#!/usr/bin/env python3


def main():
    """Run the main function of the example program."""
    print("""\
Kokeillaan käyttäjäsyötteiden lukemista silmukassa.
Anna lukuja ohjelmalle. Tyhjän rivin syöttäminen lopettaa ohjelman.
Ohjelman päätteeksi tulostetaan annettujen lukujen lukumäärä,
summa, mediaani ja keskiarvo.""")

    # Numbers provided by users will be stored in this list,
    # and printed at program termination.
    user_numbers = []

    # Start loop to request user input
    while True:
        user_number = input("Anna luku: ").strip()

        # Exit loop if no number was provided
        if not user_number:
            print("Saatiin tyhjä rivi, ei kerätä enempää lukuja.")
            break

        # Validate user input
        if user_number.isdecimal():
            # If user input is valid, append it to the list
            user_number_int = int(user_number)
            user_numbers.append(user_number_int)
        else:
            print(f"Syötä lukusi numeroin kirjoitettuna (1-9), ei auki kirjoitettuna. Kirjoitit {user_number}")
            print("Lukua ei lisätty listalle.")

    # Use the list of user provided numers
    # count
    print("\nTulostetaan annettujen lukujen lukumäärä.")
    if not user_numbers:
        print("Lukuja ei annettu.")
    elif len(user_numbers) == 1:
        print("Saatiin yksi luku.")
    else:
        print(f"Saatiin {len(user_numbers)} lukua.")

    # sum
    print("\nTulostetaan annettujen lukujen summa.")
    if not user_numbers:
        print("Lukuja ei annettu.")
    else:
        print(f"Annettujen lukujen summa on {sum(user_numbers)}")

    # median
    print("\nTulostetaan annettujen lukujen mediaani.")
    if not user_numbers:
        print("Lukuja ei annettu.")
    else:
        median = sorted(user_numbers)[int(len(user_numbers) / 2)]
        print(f"Annettujen lukujen mediaani on {median}")

    # average
    print("\nTulostetaan annettujen lukujen keskiarvo.")
    if not user_numbers:
        print("Lukuja ei annettu.")
    else:
        average = sum(user_numbers) / len(user_numbers)
        print(f"Annettujen lukujen keskiarvo on {average}")

    print("\n\n\n")
    print("Ohjelma loppuu.")


if __name__ == "__main__":
    main()
