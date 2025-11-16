from app.services.exchange_client import ExchangeClient
from app.services.cache import SimpleCache

cache = SimpleCache(ttl=15)

def get_exchange_client(exchange_name: str = "binance") -> ExchangeClient:
    return ExchangeClient(exchange_name=exchange_name)

def get_cache() -> SimpleCache:
    return cache
