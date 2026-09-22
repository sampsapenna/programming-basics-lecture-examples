number = 6

numbers_local = [
    "nolla",
    "yksi",
    "kaksi",
    "kolme",
    "neljä",
    "viisi",
    "kuusi",
    "seitsemän",
    "kahdeksan",
    "yhdeksän",
]

if number < 0:
    print("Luku oli vaaditun ulkopuolella, < 0. Käytä suurempaa lukua.")
elif number < 10:
    print(f"Annettu numero oli {numbers_local[number]}")
else:
    print(f"Annettu numero oli {number}")
