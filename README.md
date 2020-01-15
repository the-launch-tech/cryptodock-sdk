# CryptoDock Python SDK

CryptoDock SDK is a Python package used alongside the CryptoDock desktop iOS app, the CryptoDock remote API.

When bootstrapping a trading strategy in the CryptoDock desktop app the SDK is copied into the target local directory for your use in strategy development. It communicates with the remote API to pull historic and current trading data from multiple exchanges.

Additionally the SDK provides a Strategy Wrapper and Backtest Layer that is managed from the CryptoDock desktop interface.

Using this method we can normalize the structures of data from across the exchanges, run comprehensive and adaptable backtest, and provide a semantic interface, allowing for a much more efficient strategy development and research process.

## Installation

To install the SDK run: `pip install cryptodock-sdk`, or `pip install cryptodock-sdk==0.0.1`

This package will not work unless used alongside CryptoDock.

## Usage

1. (import package)

   `from sdk.cryptodock_sdk import CryptoDockSdk`

2. (initialize SDK)

   `sdk = CryptoDockSdk(base=<base_url>, port=<port>, version=<api_version>)`

## History

- Initial Release

## Credits

- Company: ©2019 The Launch
- Author: Daniel Griffiths
- Role: Founder and Engineer
- Project: ©2020 CryptoDock

## License

MIT Licence ©2020 Daniel Griffiths
