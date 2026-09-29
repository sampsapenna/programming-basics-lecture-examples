"""Functionalized version of the primes modules."""


def check_if_prime(x):
    """Check if number x is a prime.
    
    Returns >1 if the number is a prime, otherwise 1."""

    for divisor in range(2, int(x / 2)):
        if x % divisor == 0:
            return divisor

    return 1


def check_primes(range_start, range_end, show_non_primes=False):
    """Get the primes in the provided range."""

    for num in range(range_start, range_end):
        divisor = check_if_prime(num)
        if divisor == 1:
            print(f"Luku {num} on alkuluku.")
            continue
        if show_non_primes:
            print(f"Luku {num} ei ole alkuluku, jakaja on {divisor}.")


def main():
    """Calculate through primes in a loop."""
    show_non_primes = str(input("Näytetäänkö myös tavalliset luvut jakajineen? (k/E) ")) in ("k", "K")
    range_start = int(input("Mistä luvusta aloitetaan? (oletus 10)").strip() or "10")
    range_end = int(input("Mihin lukuun lopetetaan? (oletus 100)").strip() or "100")

    check_primes(range_start, range_end, show_non_primes=show_non_primes)


main()
