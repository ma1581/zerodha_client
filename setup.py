from setuptools import setup, find_packages

setup(
    name="zerodha_client",
    version="0.0.3",
    packages=find_packages(),
    install_requires=[
        "playwright==1.50.0",
        "pyotp==2.9.0",
    ],
)
