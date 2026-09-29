"""Examples of defining functions in Python."""


def is_prime(x: int):
    """Check if x is prime."""
    pass


def echo_numbers(*args):
    """Echo back the numbers in args."""
    for number in args:
        print(int(number))


def debug_echo_numbers(*args):
    print(args)

    for number in args:
        print(int(number))


def debug_kwargs(**kwargs):
    print(kwargs)


def multiple_arguments(a, b, c=3, d=4, e=5):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


def login_with_credentials(
    username: str = "test-user",
    password: str = "test-password",
    development_mode: bool = False,
):
    """Login the user using the provided credentials."""
    if not development_mode and username == "test-user":
        print("Do not use test user in production.")
    if not development_mode and password == "test-password":
        print("Do not use test password in production.")
