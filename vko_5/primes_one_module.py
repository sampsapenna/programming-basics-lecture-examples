"""Calculate a range of primes based on a given range."""


show_non_primes = False
query_show_non_primes = str(input("Näytetäänkö myös tavalliset luvut jakajineen? (k/E) "))
if query_show_non_primes == "k" or query_show_non_primes == "K":
    show_non_primes = True

range_start = int(input("Mistä luvusta aloitetaan? (oletus 10)").strip() or "10")
range_end = int(input("Mihin lukuun lopetetaan? (oletus 100)").strip() or "100")

for i in range(range_start, range_end):
    is_prime = True
    divisor = 2
    for j in range(2, int(i / 2)):
        if i % j == 0:
            is_prime = False
            divisor = j
            break

    if is_prime:
        print(f"Luku {i} on alkuluku.")
    else:
        if show_non_primes:
            print(f"Luku {i} ei ole alkuluku, jakaja {j}")
