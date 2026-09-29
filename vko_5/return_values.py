"""Examples of function return values."""


def return_before_execution(ehto: bool = True):
    print("Tämä tulostetaan ensin.")

    if ehto:
        print("Vain tämä tulostuu.")
        return

    print("Tällä kertaa tulostettiin tämä.")

    return


def get_3():
    """Return the value 3."""
    return 3

def is_prime(x: int) -> bool:
    """Check if x is prime."""
    for divisor in range(2, int(x / 2)):
        if x % divisor == 0:
            return False

    return True
