import pytest
import asyncio
from app.services.exchange_client import ExchangeClient
from app.services.cache import SimpleCache

@pytest.mark.asyncio
async def test_fetch_ticker():
    client = ExchangeClient()
    price = await client.fetch_ticker("BTC/USDT")
    assert isinstance(price, float) and price > 0
    await client.close()

@pytest.mark.asyncio
async def test_fetch_historical_ohlcv():
    client = ExchangeClient()
    ohlcv = await client.fetch_historical_ohlcv("BTC/USDT", timeframe="1d", limit=5)
    assert isinstance(ohlcv, list)
    assert len(ohlcv) > 0
    for entry in ohlcv:
        assert len(entry) == 6
    await client.close()

@pytest.mark.asyncio
async def test_simple_cache():
    cache = SimpleCache(ttl=1)
    await cache.set("test_key", "test_value")
    val = await cache.get("test_key")
    assert val == "test_value"
    await asyncio.sleep(1.1)
    val_expired = await cache.get("test_key")
    assert val_expired is None
