user_input = ""


while True:
    user_input = str(input("Jatketaanko suoritusta, [K/e]: "))

    if user_input == "e" or user_input == "E":
        print("Lopetetaan ohjelma.")
        break
    elif user_input != "K" and user_input != "k":
        print("Kielletty syöte. Sallitut syötteet: k ja e, muut syötteet kielletty.")
        print(f"Annettu syöte oli {user_input}.")
        continue
    else:
        print("Jatketaan ohjelman suorittamista.")
        continue
