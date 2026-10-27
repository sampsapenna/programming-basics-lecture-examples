"""Example of importing builtin libraries/modules."""


import math
from sys import argv
from sys import exit as sys_exit


def calculate_area(r):
    """Calculate the area of a circle with radius of r."""
    return math.pi * r ** 2


def main():
    """."""
    try:
        r = int(argv[1])
        print(f"Area of the circle is {calculate_area(r):10.2f}")
    except Exception as e:
        print(f"Got an exception when running calculate_area(): {e}")
        sys_exit(1)

    sys_exit(0)


if __name__ == "__main__":
    main()
