#!/usr/bin/env python3


import csv
import sys


def read_and_print_csv(path: str):
    """Read and print the requested csv file."""
    try:
        with open(path, "rt", newline="") as f_csv:
            file_reader = csv.reader(f_csv, delimiter=",", quotechar='"')
            file_rows = list(file_reader)

            header_row = file_rows[0]
            data_rows = file_rows[1:]

            # Print the assumed header row of the csv table
            print(f"     {header_row[0]:>10s} {header_row[1]:>10s} {header_row[2]:>10s} {header_row[3]:>20s}")

            for i in range(0, len(data_rows)):
                print(f"{(i + 1):4d} {data_rows[i][0]:>10s} {data_rows[i][1]:>10s} {data_rows[i][2]:>10s} {data_rows[i][3]:>20s}")
    except OSError as e:
        print(f"Failed to open file {path}. Reason: {e}")
        sys.exit(1)


def main():
    """Initiate the csv reader."""
    # Cache the file path
    try:
        path = sys.argv[1]
    # Mikäli komentoriviargumenttien joukossa ei ole polkua tiedostolle, lopeta ohjelman suoritus.
    except IndexError:
        print("Please provide the file path as an argument.")
        sys.exit(1)

    read_and_print_csv(path)


if __name__ == "__main__":
    main()
