# fizz = divisible by 3
# buzz = divisible by 5
# fizzbuzz = divisible by both 3 and 5


# fizzbuzz from numbers 0-100

for i in range(0, 101):
    if i % 3 == 0:
        print("fizz", end="")
    if i % 5 == 0:
        print("buzz", end="")
    if i % 3 != 0 and i % 5 != 0:
        print(i, end="")
    print(" ", end="")

print("")
