import ccxt.async_support as ccxt_async
from typing import Optional, List


class ExchangeClient:
    def __init__(self, exchange_name: str = "binance"):
        exchange_class = getattr(ccxt_async, exchange_name)
        if exchange_name.lower() == "binance":
            self.exchange = exchange_class({
                'options': {
                    'defaultType': 'spot'
                }
            })
        else:
            self.exchange = exchange_class()
        self.supported_exchanges = ["binance", "coinbasepro", "kraken"]

    async def fetch_ticker(self, symbol: str) -> float:
        try:
            ticker = await self.exchange.fetch_ticker(symbol)
            return float(ticker["last"])
        except Exception as e:
            raise RuntimeError(f"Failed to fetch ticker for {symbol}: {e}")

    async def fetch_historical_ohlcv(self, symbol: str, timeframe: str = "1d", since: Optional[int] = None, limit: int = 100) -> List[List]:
        try:
            ohlcv = await self.exchange.fetch_ohlcv(symbol, timeframe=timeframe, since=since, limit=limit)
            return ohlcv
        except Exception as e:
            raise RuntimeError(f"Failed to fetch historical OHLCV for {symbol}: {e}")

    async def close(self):
        await self.exchange.close()
