"""Context manager example"""

import secrets


def write_with_ctx():
    """Write tokens to file, use context manager."""
    # Context manager closes the file when exiting the context
    with open("generated_tokens.txt", "w") as f:
        # Generate 10 tokens to the file
        for _ in range(0, 10):
            f.write(f"{secrets.token_urlsafe(64)}\n")


write_with_ctx()
