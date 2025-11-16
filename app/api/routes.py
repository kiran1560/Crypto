from fastapi import APIRouter, HTTPException, Query
from app.services.exchange_client import ExchangeClient
from app.services.cache import SimpleCache
from app.models.schemas import PriceResponse, HistoricalResponse, ErrorResponse
from typing import Optional

router = APIRouter()
cache = SimpleCache(ttl=15)

SUPPORTED_EXCHANGES = ["binance", "kraken", "coinbasepro"]

@router.get("/realtime/{symbol}", response_model=PriceResponse, responses={500: {"model": ErrorResponse}})
async def get_realtime_price(
    symbol: str,
    exchange: str = Query("binance", regex="^(binance|kraken|coinbasepro)$")
):
    cached = await cache.get(f"realtime_{exchange}_{symbol}")
    if cached:
        return cached

    try:
        client = ExchangeClient(exchange_name=exchange)
        price = await client.fetch_ticker(symbol)
        await client.close()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    response = PriceResponse(symbol=symbol, price=price)
    await cache.set(f"realtime_{exchange}_{symbol}", response)
    return response


@router.get("/historical/{symbol}", response_model=HistoricalResponse, responses={500: {"model": ErrorResponse}})
async def get_historical_prices(
    symbol: str,
    timeframe: str = Query("1d", regex="^(1m|5m|15m|30m|1h|4h|1d|1w)$"),
    limit: int = Query(100, ge=1, le=1000),
    exchange: str = Query("binance", regex="^(binance|kraken|coinbasepro)$")
):
    cache_key = f"historical_{exchange}_{symbol}_{timeframe}_{limit}"
    cached = await cache.get(cache_key)
    if cached:
        return cached

    try:
        client = ExchangeClient(exchange_name=exchange)
        ohlcv = await client.fetch_historical_ohlcv(symbol, timeframe=timeframe, limit=limit)
        await client.close()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    data = [
        {
            "timestamp": entry[0],
            "open": entry[1],
            "high": entry[2],
            "low": entry[3],
            "close": entry[4],
            "volume": entry[5],
        }
        for entry in ohlcv
    ]

    response = HistoricalResponse(symbol=symbol, timeframe=timeframe, data=data)
    await cache.set(cache_key, response)
    return response
