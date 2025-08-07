import base64
from typing import Tuple


def reverse_encoded_password(encoded: str) -> Tuple[str, str, str]:
    """
    Reverse an M-PESA base64-encoded password.

    Args:
        encoded (str): The base64-encoded password.

    Returns:
        Tuple[str, str, str]: A tuple containing:
            - BusinessShortCode (str)
            - Passcode (str)
            - Timestamp (str in YYYYMMDDHHMMSS format)
    """
    try:
        # Decode from base64
        decoded = base64.b64decode(encoded).decode("utf-8")
    except Exception as e:
        raise ValueError(f"Invalid base64 encoding: {e}")

    # Timestamp is always the last 14 digits
    timestamp = decoded[-14:]

    # Assume BusinessShortCode is the first 6 digits
    shortcode = decoded[:6]

    # Everything in between is the passcode
    passcode = decoded[6:-14]

    return shortcode, passcode, timestamp


# Example usage
if __name__ == "__main__":
    encoded_password = (
        "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5"
        "YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjUwODA2MTQzNjQ0"
    )

    shortcode, passcode, timestamp = reverse_encoded_password(encoded_password)

    print("BusinessShortCode:", shortcode)
    print("Passcode:", passcode)
    print("Timestamp:", timestamp)
