#!/usr/bin/env python3


def main():
    """Run the main function of the example program."""
    print("Kokeillaan käyttäjäsyötteiden lukemista.")

    # Varsinainen käyttäjäsyötteen lukeminen tähän kohtaan
    user_input = input("Kirjoita jotakin (ja paina lopuksi enter/rivinvaihto): ")
    print(f"Kirjoitit: {user_input}")

    print("\n\n\n")
    user_input_2 = input("Anna henkilöiden sukunimet välilyönnillä eroteltuna: ")
    # Covert user_input_2 to list based on separation by spaces
    user_input_2_list = user_input_2.split(" ")
    for name in user_input_2_list:
        print(f"Syötit nimen: {name}")

    print("\n\n\n")
    user_input_3 = input("Anna henkilöiden sukunimet pilkulla eroteltuna: ")
    user_input_3_list = user_input_3.split(",")

    # Clean up unnecessary whitespace
    user_input_3_list = [name.strip() for name in user_input_3_list]
    for name in user_input_3_list:
        print(f"Syötit nimen: {name}")

    # Logically equivalent to
    user_input_3_list_stripped = []
    for name in user_input_3_list:
        user_input_3_list_stripped.append(name.strip())
    user_input_3_list = user_input_3_list_stripped

    print("\n\n\n")
    print("Ohjelma loppuu.")


if __name__ == "__main__":
    main()
