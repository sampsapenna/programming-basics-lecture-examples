number = 0
string = ""


ZERO = "nolla"
ONE = "yksi"
TWO = "kaksi"
THREE = "kolme"
FOUR = "neljä"
FIVE = "viisi"
SIX = "kuusi"
SEVEN = "seitsemän"
EIGHT = "kahdeksan"
NINE = "yhdeksän"


if number == 0:
    # Substitute with the placholder for zero
    string = ZERO
elif number == 1:
    # Substitutewith the placeholder for one
    string = ONE
elif number == 2:
    # Substitute with the placeholder for two
    string = TWO
elif number == 3:
    # Substitute with the placeholder for three
    string = THREE
elif number == 4:
    # Substitute with the placeholder for four
    string = FOUR
elif number == 5:
    # Substitute with the placeholder for five
    string = FIVE
elif number == 6:
    # Substitute with the placeholder for six
    string = SIX
elif number == 7:
    # Substitute with the placeholder for seven
    string = SEVEN
elif number == 8:
    # Substitute with the placeholder for eight
    string = EIGHT
elif number == 9:
    # Substitute with the placeholder for nine
    string = NINE
else:
    string = f"{number}"

print(f"Annettu numero oli {string}.")
