"""Generate M-Pesa Security Credential using an initiator password and public key encryption."""

import os
import base64
from datetime import datetime
from typing import Optional

from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey

# Default cert directory (relative to this file)
DEFAULT_CERT_DIR = os.path.join(os.path.dirname(__file__), "certs")


def _default_cert_path(environment: str) -> str:
    """Get the default certificate path based on the environment."""
    filename = (
        "ProductionCertificate.cer"
        if environment == "production"
        else "SandboxCertificate.cer"
    )
    return os.path.join(DEFAULT_CERT_DIR, filename)


def _load_public_key_from_cert(cert_path: str) -> RSAPublicKey:
    """Load an RSA public key from a certificate file. Supports PEM and DER encoded X.509 certs."""
    if not os.path.isfile(cert_path):
        raise FileNotFoundError(f"Certificate not found at: {cert_path}")

    data = open(cert_path, "rb").read()

    # Load PEM certificate
    try:
        cert = x509.load_pem_x509_certificate(data)
        public_key = cert.public_key()
        if isinstance(public_key, RSAPublicKey):
            return public_key
        else:
            raise ValueError("The certificate does not contain an RSA public key.")
    except Exception as e:
        raise ValueError(f"Could not load a valid PEM X.509 certificate: {e}")


def generate_security_credential(
    initiator_password: str,
    cert_path: Optional[str] = None,
    environment: str = "sandbox",
) -> str:
    """Generate an M-Pesa Security Credential using an initiator password.

    Algorithm:
    1. Write the unencrypted password into a byte array: password = initiator_password + timestamp.
    2. Encrypt the byte array using the M-Pesa RSA public key with PKCS#1 v1.5 padding.
    3. Base64-encode the encrypted bytes and return the resulting string.

    :param initiator_password: M-Pesa initiator password
    :param cert_path: Path to .cer file. If None, defaults by environment.
    :param environment: "production" or "sandbox"
    :return: Base64-encoded encrypted security credential
    """
    if not initiator_password:
        raise ValueError("Initiator password is required.")

    if cert_path is None:
        cert_path = _default_cert_path(environment)

    public_key = _load_public_key_from_cert(cert_path)

    # Step 1: timestamp and unencrypted password bytes
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    password_bytes = f"{initiator_password}{timestamp}".encode("utf-8")

    # Step 2: encrypt using RSA PKCS#1 v1.5 padding (M-Pesa expects this)
    try:
        encrypted_bytes = public_key.encrypt(password_bytes, padding.PKCS1v15())
    except Exception as e:
        raise RuntimeError(f"Encryption failed: {e}")

    # Step 3: base64-encode and return string
    return base64.b64encode(encrypted_bytes).decode("utf-8")
