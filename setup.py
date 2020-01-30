from pathlib import Path
from setuptools import find_packages, setup

setup(
    name="cryptodock-sdk",
    version="0.1.3",
    description="SDK for CryptoDock's remote API. The SDK is meant to be leveraged with CryptoDock Strategy Framework and the CryptoDock Suite. The SDK provides a semantic interface for placing orders, and getting cloud-stored historic data as well as current exchange data from multiple exchanges through the remote NodeJS CryptoDock Remote API. This data has been normalized so that the naming conventions and structures are similar regardless of the source exchange's API",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/the-launch-tech/cryptodock-sdk",
    author="Daniel Griffiths",
    author_email="daniel@thelaunch.tech",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["requests"]
)
