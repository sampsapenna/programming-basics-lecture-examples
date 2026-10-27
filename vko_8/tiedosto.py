"""File use examples."""


def main():
    print("Tulostetaan tiedosto requirements.txt")

    f = open("requirements.txt", "r")
    for line in f.readlines():
        print(line, end="")

    return 0


if __name__ == "__main__":
    main()
