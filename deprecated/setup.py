import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mpesa-py",
    version="1.0",
    author="Aurlus Ismael Wedava",
    author_email="arlusishmael@gmail.com",
    description="A Python wrapper for Mpesa Daraja APIs.",
    long_description="This library provides thin wrappers around Mpesa Daraja APIs. The APIs supported are Reversal, Transaction Status, Account Balance, B2B, B2C, C2B and MPESA Express",
    url="https://github.com/Arlus/mpesa-py",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'certifi', 'chardet==3.0.4', 'future==0.16.0', 'idna==2.7', 'requests==2.20.0',
        'six==1.11.0', 'urllib3==1.26.5', 'pytest==3.6.1 '
    ],
)
