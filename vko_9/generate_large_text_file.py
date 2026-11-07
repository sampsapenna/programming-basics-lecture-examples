#!/usr/bin/env python3


import secrets


def main():
    """Generate a large amount of random URL safe text."""
    output = [
        f"Row {i} random token is {secrets.token_urlsafe(100)}\n" for i in range(1, 10000001)
    ]

    with open("large_text_file.txt", "w") as f:
        f.writelines(output)


if __name__ == "__main__":
    main()
