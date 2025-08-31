---
title: Environment Configuration
description: Recommends and shows how one can use the credentials without hardcoding credentials in your code.
slug: /environment
sidebar_label: Environment Configuration
tags:

- setup
- env-config

---

- Add your M-Pesa credentials to your environment (for example, a `.env` file). This file is a recommendation to avoid hardcoding keys in your code
- Do not commit secrets to version control. Use a secrets manager or CI/CD environment variables for production.

As we continue through the documentation, examples will read credentials using os.getenv(...) to show which environment variables are expected. For example:

```python
import os

MPESA_CONSUMER_KEY = os.getenv("MPESA_CONSUMER_KEY")
MPESA_CONSUMER_SECRET = os.getenv("MPESA_CONSUMER_SECRET")
MPESA_ENVIRONMENT = os.getenv("MPESA_ENVIRONMENT", "sandbox")
MPESA_BUSINESS_SHORTCODE = os.getenv("MPESA_BUSINESS_SHORTCODE")
MPESA_PASSKEY = os.getenv("MPESA_PASSKEY")
MPESA_SECURITY_CREDENTIAL = os.getenv("MPESA_SECURITY_CREDENTIAL")
```

This is a recommendation only. The goal is to prevent embedding direct keys in code and keep secrets out of source control.

## Sandbox example

```text
MPESA_CONSUMER_KEY=your_sandbox_consumer_key
MPESA_CONSUMER_SECRET=your_sandbox_consumer_secret
MPESA_ENVIRONMENT=sandbox
MPESA_BUSINESS_SHORTCODE=174379  # Default sandbox shortcode
MPESA_PASSKEY="bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c91"  # Sandbox default
MPESA_SECURITY_CREDENTIAL=<will_get_from_the_api_app_created>
```

## Production example

```text
MPESA_CONSUMER_KEY=your_production_consumer_key
MPESA_CONSUMER_SECRET=your_production_consumer_secret
MPESA_ENVIRONMENT=production
MPESA_BUSINESS_SHORTCODE=your_production_shortcode
MPESA_PASSKEY="your_production_passkey"
MPESA_SECURITY_CREDENTIAL=<production_security_credential_from_api_app>
```

## Notes

- MPESA_SECURITY_CREDENTIAL is generated from the API app [see how to create/get it](/getting-credentials).
- Keep secrets out of source control; use a secrets manager or environment variables in deployment.
- For more details on where to get these values, see [/getting-credentials](/getting-credentials)
