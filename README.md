MCP Server - Cryptocurrency Market Data Provider

Overview
FastAPI server providing real-time and historical crypto data from multiple exchanges via CCXT.
Supports Binance, Kraken, and Coinbase Pro with caching and error handling.

Setup and Run: Create and activate virtual environment

python -m venv venv
# On Windows, activate with:
# venv\Scripts\activate
source venv/bin/activate  # For Linux/macOS

Install dependencies:
pip install -r requirements.txt

Run the server with auto-reload:
uvicorn app.main:app --reload

Testing:
pytest app/tests/

Approach Summary

Uses FastAPI with asynchronous CCXT to fetch data from multiple exchanges.
ExchangeClient handles API calls; exchange is selectable per request.
Implements simple caching to reduce redundant external API calls.
Normalizes trading symbols according to each exchange’s format.
Provides clear error handling and returns structured API errors.
