# MCP Server - Cryptocurrency Market Data Provider

# Overview:
# FastAPI server providing real-time and historical crypto data from multiple exchanges via CCXT.
# Supports Binance, Kraken, and Coinbase Pro with caching and error handling.


# Create and activate virtual environment
python -m venv venv
# venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run server with auto-reload
uvicorn app.main:app --reload

# Server URL: http://127.0.0.1:8000
# API docs: http://127.0.0.1:8000/docs



# Run tests
pytest app/tests/

# --- Approach ---

# - Uses FastAPI and async CCXT to fetch data from multiple exchanges.
# - ExchangeClient handles API calls; exchange selectable per request.
# - Simple caching reduces redundant API calls.
# - Symbols normalized per exchange format.
# - Error handling returns clear API errors.
# - Pydantic models ensure data validation.
# - Async design supports concurrent requests efficiently.

