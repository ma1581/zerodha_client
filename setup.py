from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="zerodha_client",
    version="0.0.4",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "playwright==1.50.0",
        "pyotp==2.9.0",
    ],
)
