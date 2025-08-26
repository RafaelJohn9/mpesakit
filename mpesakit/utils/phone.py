"""Utility functions for handling phone numbers in the M-Pesa SDK."""


def normalize_phone_number(phone: str) -> str | None:
    """Normalize a Kenyan phone number to the '2547XXXXXXXX' format.

    - If it starts with '0', replace with '254'
    - If it starts with '+254', replace with '254'
    - If it starts with '254', return as is
    - Handles whitespace anywhere in the number
    - Otherwise, return None

    Args:
        phone (str): The phone number to normalize.

    Returns:
        str | None: Normalized phone number or None if invalid.
    """
    if not isinstance(phone, str):
        return None
    phone = phone.strip().replace(" ", "")
    normalized = None
    if phone.startswith("+254") and len(phone) == 13:
        normalized = "254" + phone[4:]
    elif phone.startswith("0") and len(phone) == 10:
        normalized = "254" + phone[1:]
    elif phone.startswith("254") and len(phone) == 12:
        normalized = phone

    if (
        normalized
        and normalized.isdigit()
        and len(normalized) == 12
        and normalized.startswith("2547")
    ):
        return normalized
    else:
        return None
