# mpesa-daraja-sdk

> ⚡ **Effortless M-Pesa integration** using Safaricom's Daraja API — built for developers, by developers.

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://opensource.org/licenses/Apache-2.0)
<!-- [![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]() -->

---

## The Problem

Integrating Safaricom's **M-Pesa Daraja API** directly is **notoriously complex**:

- Confusing and inconsistent documentation
- Manual handling of OAuth2 tokens and security credentials
- Complex encryption and certificate management
- Different endpoints for sandbox vs production environments
- STK Push, C2B, B2C, balance — all feel like separate APIs
- Time-consuming setup that delays your time-to-market

For many developers and startups, this becomes a **huge barrier** to adopting M-Pesa payments in Kenya and beyond.

---

## The Solution

**`mpesa-daraja-sdk`** eliminates the complexity with a **clean, developer-friendly Python SDK** that:

- **Zero-config setup** — just add your credentials and go
- **Handles authentication automatically** — OAuth2, tokens, and security
- **Seamless environment switching** — sandbox ↔ production with one parameter
- **Pythonic interface** — clean methods that feel natural to Python developers
- **Batteries included** — everything you need for M-Pesa integration
- **Production-ready** — end goal is to be used by startups and enterprises across Kenya

### Supported Features

| Feature | Status | Description |
|---------|--------|-------------|
| **STK Push** | Ready | Lipa na M-Pesa Online payments |
| **C2B Payments** | Ready | Customer to Business transactions |
| **B2C Payments** | Ready | Business to Customer payouts |
| **Token Management** | Ready | Automatic OAuth2 handling |
| **Account Balance** | Coming Soon | Check account balances |
|  **Transaction Reversal** | Coming Soon | Reverse transactions |
| 🎣 **Webhook Validation** | Coming Soon | Secure callback handling |

> Built on top of [Arlus/mpesa-py](https://github.com/Arlus/mpesa-py) with ❤️ — modernized, cleaned up, and restructured for today's developer needs.

---

## Quick Start

### Installation (coming soon)

```bash
pip install mpesa-daraja-sdk
```

---

## 📖 Complete Setup Guide

### 1. Get Safaricom Developer Account

1. Visit [developer.safaricom.co.ke](https://developer.safaricom.co.ke)
2. **Create account** and verify your email
3. **Create a new app** to get your credentials:
   - Consumer Key
   - Consumer Secret

### 2. Obtain Test Credentials (Sandbox)

1. Navigate to [Test Credentials Page](https://developer.safaricom.co.ke/test_credentials)
2. Copy the following credentials:
   - **Shortcode** (Business number)
   - **Initiator Name** (API operator username)
   - **Initiator Password** (API operator password)
   - **Security Credential** (Encrypted password)

### 3. Production Setup

For production deployment:

1. **Get Paybill/Till Number** from Safaricom
2. **Generate Security Credential** using Safaricom's public certificate
3. **Switch environment** to `"production"` in your client initialization
4. **Update callback URLs** to your production domain

---

### Security Best Practices

1. **Never commit credentials** to version control
2. **Use environment variables** for sensitive data
3. **Implement webhook validation** for callbacks
4. **Log transactions** for audit trails
5. **Monitor rate limits** and implement backoff strategies
6. **Use HTTPS** for all callback URLs

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Ways to Contribute

- 🐛 **Report bugs** via GitHub Issues
- 💡 **Suggest features** for the roadmap
- 📖 **Improve documentation** and examples
- 🔧 **Submit pull requests** with fixes/features
- ⭐ **Star the repo** to show support

### Development Setup

```bash
# Clone the repository
git clone https://github.com/rafaeljohn9/mpesa-daraja-sdk.git
cd mpesa-daraja-sdk

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest tests/
```

### Code Standards

- Follow PEP 8 style guidelines
- Include type hints where appropriate
- Write comprehensive tests for new features
- Update documentation for any API changes

---

## 📞 Support & Community

- 📖 **Documentation**: [Full API docs coming soon]
- 🐛 **Issues**: [GitHub Issues](https://github.com/rafaeljohn9/mpesa-daraja-sdk/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/rafaeljohn9/mpesa-daraja-sdk/discussions)
- 📧 **Email**: <johnmkagunda@gmail.com>

---

## 🙏 Attribution & Thanks

This project began as a fork of the fantastic [`Arlus/mpesa-py`](https://github.com/Arlus/mpesa-py) by [@Arlus](https://github.com/Arlus).

**What we've added:**

- 🏗️ **Modular architecture** for better maintainability
- 🎯 **Developer-first design** with intuitive APIs
- 🧪 **Comprehensive testing** suite
- 📚 **Better documentation** and examples
- 🚀 **Production-ready** features and error handling

Special thanks to the original contributors and the broader Python community in Kenya.

---

## 📄 License

Licensed under the [Apache 2.0 License](LICENSE) — free for commercial and private use.

---

<div align="center">

**Made with ❤️ for the Kenyan developer community**

[⭐ Star this repo](https://github.com/rafaeljohn9/mpesa-daraja-sdk) | [🐛 Report Issue](https://github.com/rafaeljohn9/mpesa-daraja-sdk/issues) | [💡 Request Feature](https://github.com/rafaeljohn9/mpesa-daraja-sdk/issues/new)

</div>
