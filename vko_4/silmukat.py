# Esimerkki, käyttäen for-silmukkaa
for i in range(0, 100):
    if i % 10 == 0 and i > 0:
        print(f"The value i is {i}, and i is divisible by 10.")

print("\n\n\n")

# Sama esimerkki, käyttäen while-silmukkaa
i = 0
while True:
    i += 1

    if not (i % 10 == 0 and i > 0):
        continue

    if i > 200:
        break
            
    print(f"The value i is {i}, and i is divisible by 10.")
