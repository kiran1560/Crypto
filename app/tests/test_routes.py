import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_root_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the MCP Crypto Market Data API"}

@pytest.mark.asyncio
async def test_realtime_price_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/realtime/BTC/USDT")
    if response.status_code == 422:
        response = await ac.get("/api/realtime/BTCUSDT")
    assert response.status_code == 200
    data = response.json()
    assert "symbol" in data and "price" in data

@pytest.mark.asyncio
async def test_historical_price_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/historical/BTC/USDT?timeframe=1d&limit=5")
    if response.status_code == 422:
        response = await ac.get("/api/historical/BTCUSDT?timeframe=1d&limit=5")
    assert response.status_code == 200
    data = response.json()
    assert "symbol" in data and "timeframe" in data and "data" in data
    assert isinstance(data["data"], list)
