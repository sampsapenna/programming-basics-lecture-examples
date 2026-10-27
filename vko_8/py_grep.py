"""Small simple grep implementation in python."""


import sys


def main():
    """Grep lines containing the word in file."""
    path = sys.argv[1]
    to_grep = sys.argv[2]

    try:
        f = open(path, "r")

        line = f.readline()
        while line:
            if to_grep in line:
                print(line, end="")
            line = f.readline()

        # while line := f.readline():
        #     if to_grep in line:
        #         print(line, end="")

        f.close()
        sys.exit(0)
    except OSError:
        print(f"Could not open file {path}")
        sys.exit(1)


if __name__ == "__main__":
    main()
