"""Unit tests for generate_security_credential in mpesakit.security.get_credential."""

import base64
from datetime import datetime, timedelta, timezone
import pytest
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, padding as asym_padding, rsa
from cryptography.x509.oid import NameOID
from mpesakit.security.get_credential import generate_security_credential


def _create_self_signed_cert_rsa(tmp_path):
    """Create a self-signed RSA certificate for testing."""
    # Generate RSA key
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    subject = issuer = x509.Name(
        [x509.NameAttribute(NameOID.COMMON_NAME, "test.local")]
    )
    now = datetime.now(timezone.utc)
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(public_key)
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - timedelta(days=1))
        .not_valid_after(now + timedelta(days=10))
        .add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True)
        .sign(private_key, hashes.SHA256())
    )

    cert_path = tmp_path / "rsa_cert.pem"
    cert_path.write_bytes(cert.public_bytes(serialization.Encoding.PEM))
    return private_key, str(cert_path)


def _create_self_signed_cert_ec(tmp_path):
    """Create a self-signed EC certificate for testing (non-RSA)."""
    # Generate EC key (non-RSA)
    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key()

    subject = issuer = x509.Name(
        [x509.NameAttribute(NameOID.COMMON_NAME, "test.local")]
    )
    now = datetime.now(timezone.utc)
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(public_key)
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - timedelta(days=1))
        .not_valid_after(now + timedelta(days=10))
        .add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True)
        .sign(private_key, hashes.SHA256())
    )

    cert_path = tmp_path / "ec_cert.pem"
    cert_path.write_bytes(cert.public_bytes(serialization.Encoding.PEM))
    return private_key, str(cert_path)


def test_generate_security_credential_success_rsa(tmp_path):
    """Generating credential with a valid RSA certificate.

    Which should produce a base64 string that decrypts to initiator_password + 14-digit timestamp.
    """
    initiator_password = "s3cr3t!"
    private_key, cert_path = _create_self_signed_cert_rsa(tmp_path)

    sec_cred_b64 = generate_security_credential(initiator_password, cert_path=cert_path)
    assert isinstance(sec_cred_b64, str) and sec_cred_b64 != ""

    encrypted = base64.b64decode(sec_cred_b64)
    decrypted = private_key.decrypt(encrypted, asym_padding.PKCS1v15())
    # decrypted should be initiator_password + timestamp (14 digits)
    assert decrypted.startswith(initiator_password.encode("utf-8"))
    timestamp_bytes = decrypted[len(initiator_password) :]
    assert len(timestamp_bytes) == 14
    assert timestamp_bytes.decode("utf-8").isdigit()


def test_generate_security_credential_missing_cert():
    """If the certificate file does not exist, FileNotFoundError is raised."""
    with pytest.raises(FileNotFoundError):
        generate_security_credential("pw", cert_path="/non/existent/path.pem")


def test_generate_security_credential_empty_initiator_password(tmp_path):
    """Empty initiator password should raise a ValueError before attempting to load cert."""
    # create a valid cert to ensure error is from empty password, not cert loading
    _, cert_path = _create_self_signed_cert_rsa(tmp_path)
    with pytest.raises(ValueError):
        generate_security_credential("", cert_path=cert_path)


def test_generate_security_credential_with_non_rsa_cert_raises_value_error(tmp_path):
    """A certificate with a non-RSA public key should raise ValueError when loading RSA public key."""
    _, cert_path = _create_self_signed_cert_ec(tmp_path)
    with pytest.raises(ValueError):
        generate_security_credential("pw", cert_path=cert_path)


def test_generate_security_credential_with_invalid_cert_bytes(tmp_path):
    """A corrupt/invalid cert file should raise a ValueError from the loader."""
    bad_path = tmp_path / "bad_cert.pem"
    bad_path.write_bytes(b"not a certificate")
    with pytest.raises(ValueError):
        generate_security_credential("pw", cert_path=str(bad_path))
