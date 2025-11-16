from typing import List, Optional
from pydantic import BaseModel


class PriceResponse(BaseModel):
    symbol: str
    price: float


class OHLCVData(BaseModel):
    timestamp: int
    open: float
    high: float
    low: float
    close: float
    volume: float


class HistoricalResponse(BaseModel):
    symbol: str
    timeframe: str
    data: List[OHLCVData]


class ErrorResponse(BaseModel):
    detail: str
