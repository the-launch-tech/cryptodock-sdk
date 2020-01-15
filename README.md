# CryptoDock Python SDK

CryptoDock SDK is a Python package used alongside the CryptoDock desktop iOS app, the CryptoDock remote API.

When bootstrapping a trading strategy in the CryptoDock desktop app the SDK is copied into the target local directory for your use in strategy development. It communicates with the remote API to pull historic and current trading data from multiple exchanges.

Additionally the SDK provides a Strategy Wrapper and Backtest Layer that is managed from the CryptoDock desktop interface.

Using this method we can normalize the structures of data from across the exchanges, run comprehensive and adaptable backtest, and provide a semantic interface, allowing for a much more efficient strategy development and research process.

## Installation

To install the SDK run: `pip install cryptodock-sdk`, or `pip install cryptodock-sdk==0.0.1`

This package will not work unless used alongside CryptoDock.

## Usage

### Import Package(s)

- `from cryptodock import CryptoDockSdk`
- `from cryptodock import CryptoDockApi, CryptoDockStrategy, CryptoDockBacktest`

### Initialize SDK

- `full_sdk = CryptoDockSdk()`
- `full_sdk.Api.Local.get_products(exchanges="coinbasepro")`
- `full_sdk.Strategy`
- `full_sdk.Backtest(<your_strategy>)`

- `api = CryptoDockApi(base=<base_url>, port=<port>, version=<api_version>)`
- `api.Local.get_exchanges()`
- `api.CoinbasePro.get_trade_histories('BTC-USDT')`

- `YourStrategy(CryptoDockStrategy)`

- `backtest = CryptoDockBacktest(YourStrategy)`
- `backtest.run_test(data)`

## History

- Initial Release
- Integrating backtest and strategy wrapper, not just api sdk

## Credits

- Company: ©2019 The Launch
- Author: Daniel Griffiths
- Role: Founder and Engineer
- Project: ©2020 CryptoDock

## License

MIT Licence ©2020 Daniel Griffiths
