# mpesakit

> ⚡ **Effortless M-Pesa integration** using Safaricom's Daraja API — built for developers, by developers.

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://opensource.org/licenses/Apache-2.0)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

[![PyPI version](https://img.shields.io/pypi/v/mpesakit.svg)](https://pypi.org/project/mpesakit) [![Downloads](https://pepy.tech/badge/mpesakit)](https://pepy.tech/project/mpesakit)
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

**`mpesakit`** eliminates the complexity with a **clean, developer-friendly Python SDK** that:

- **Zero-config setup** — just add your credentials and go
- **Handles authentication automatically** — OAuth2, tokens, and security
- **Seamless environment switching** — sandbox ↔ production with one parameter
- **Pythonic interface** — clean methods that feel natural to Python developers
- **Batteries included** — everything you need for M-Pesa integration
- **Production-ready** — end goal is to be used by startups and enterprises across Kenya

### Supported Features

| Feature | Status | Description |
|---------|--------|-------------|
| **STK Push (Lipa na M-Pesa)** | Ready | Initiate customer payment prompts (mpesa-express/stk-push.mdx) |
| **STK Query** | Ready | Query STK push/payment status (mpesa-express/stk-query.mdx) |
| **C2B Payments** | Ready | Customer-to-Business payments (c2b.mdx) |
| **B2C Payments** | Ready | Business-to-Customer payouts (b2c.mdx) |
| **B2C Account Top-up** | Ready | Account top-up flows for B2C (b2c-account-top-up.mdx) |
| **Business Paybill** | Ready | Paybill integrations for business collections (business-paybill.mdx) |
| **Business BuyGoods** | Ready | Till/BuyGoods integrations (business-buygoods.mdx) |
| **Token Management / Auth** | Ready | Automatic OAuth2 handling and auth utilities (auth.mdx) |
| **Account Balance** | Ready | Check account balances (account-balance.mdx) |
| **Transaction Reversal** | Ready | Reverse transactions (reversal.mdx) |
| **Transaction Status** | Ready | Query transaction status (transaction-status.mdx) |
| **Dynamic QR** | Ready | Generate and manage dynamic QR payments (dynamic-qr.mdx) |
| **Tax Remittance** | Ready | Tax remittance flows and docs (tax-remittance.mdx) |

> Built on top of [Arlus/mpesa-py](https://github.com/Arlus/mpesa-py) with ❤️ — modernized, cleaned up, and restructured for today's developer needs.

---

## Quick Start

### Installation (already here :) )

```bash
pip install mpesakit
```

---

## 📖 Complete Setup Guide

- For the complete setup guide kindly check the documentation at: [https://mpesakit.dev](https://mpesakit.dev)

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
git clone https://github.com/rafaeljohn9/mpesakit.git
cd mpesakit

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest tests/unit
```

### Code Standards

- Follow PEP 8 style guidelines
- Include type hints where appropriate
- Write comprehensive tests for new features
- Update documentation for any API changes

---

## 📞 Support & Community

- 📖 **Documentation**: [Full API docs coming soon]
- 🐛 **Issues**: [GitHub Issues](https://github.com/rafaeljohn9/mpesakit/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/rafaeljohn9/mpesakit/discussions)
- 📧 **Email**: <johnmkagunda@gmail.com>

---

## 🙏 Attribution & Thanks

This project began as a fork of the fantastic [`Arlus/mpesa-py`](https://github.com/Arlus/mpesa-py) by [@Arlus](https://github.com/Arlus).

**What we've added:**

- **Modular architecture** for better maintainability
- **Developer-first design** with intuitive APIs
- **Comprehensive testing** suite
- **Better documentation** and examples
- **Production-ready** features and error handling

Special thanks to the original contributors and the broader Python community in Kenya.

---

## 📄 License

Licensed under the [Apache 2.0 License](LICENSE) — free for commercial and private use.

---

<div align="center">

**Made with ❤️ for the Kenyan developer community**

[⭐ Star this repo](https://github.com/rafaeljohn9/mpesakit) | [🐛 Report Issue](https://github.com/rafaeljohn9/mpesakit/issues) | [💡 Request Feature](https://github.com/rafaeljohn9/mpesakit/issues/new)

</div>
