#!/usr/bin/env python3


def main():
    """Run the main function of the example program."""
    print("Kokeillaan käyttäjäsyötteiden lukemista ja muutamista.")
    print("\n\n\n")

    # .strip() following input() to remove whitespace before and after input
    user_number = input("Anna numero: ").strip()

    # Let's convert user number to an integer safely
    # Option one – try-except
    try:
        user_number_1 = int(user_number)
        print(f"Annoit numeron {user_number_1:d}")
    except ValueError:
        print(f"Syötä numerosi numeroin kirjoitettuna (1-9), ei auki kirjoitettuna. Kirjoitit {user_number}")

    # Option two – str.isdecimal()
    if user_number.isdecimal():
        user_number_2 = int(user_number)
        print(f"Annoit numeron {user_number_2:d}")
    else:
        print(f"Syötä numerosi numeroin kirjoitettuna (1-9), ei auki kirjoitettuna. Kirjoitit {user_number}")

    print("\n\n\n")

    # .strip() following input() to remove whitespace before and after input
    user_float = input("Anna liuluku. Desimaalierottimena toimii piste (.): ").strip()

    # Let's convert user number to a float safely
    # Option one – try-except
    try:
        user_float_1 = float(user_float)
        print(f"Annoit liukuluvun {user_float_1:f}")
    except ValueError:
        print(f"Syötä numerosi kirjoitettuna numeroin (1-9), piste desimaalierottimena. Kirjoitit {user_float}")
    # Option two – str.replace + str.isdecimal
    # Replace the decimal separator to allow checking that user input only
    # contains numeric characters, replace only one instance of a . to
    # ensure that there aren't multiple decimal separators.
    if user_float.replace(".", "", 1).isdecimal():
        user_float_2 = float(user_float)
        print(f"Annoit liukuluvun {user_float_2:f}")
    else:
        print(f"Syötä numerosi kirjoitettuna numeroin (1-9), piste desimaalierottimena. Kirjoitit {user_float}")

    print("\n\n\n")
    print("Ohjelma loppuu.")


if __name__ == "__main__":
    main()
