
<body>

<h1>MCP Server - Cryptocurrency Market Data Provider</h1>

<section>
  <h2>Overview</h2>
  <p>
    This project is a FastAPI-based server that provides real-time and historical cryptocurrency market data from multiple major exchanges using the CCXT library. It supports Binance, Kraken, and Coinbase Pro exchanges and includes caching and error handling for robust API performance.
  </p>
</section>

<section>
  <h2>Features</h2>
  <ul>
    <li>Real-time price retrieval for supported trading pairs</li>
    <li>Historical OHLCV data fetching with customizable timeframe and limit</li>
    <li>Support for multiple exchanges, selectable per request</li>
    <li>In-memory caching to reduce redundant API calls</li>
    <li>Clear error handling and structured JSON responses</li>
    <li>Asynchronous implementation for high concurrency</li>
    <li>Data validation and automatic API docs powered by Pydantic</li>
  </ul>
</section>

<section>
  <h2>Setup</h2>
  <ol>
    <li>
      Create and activate a Python virtual environment:
      <pre><code>python -m venv venv
# Activate the environment:
venv\Scripts\activate
      </code></pre>
    </li>
    <li>
      Install required dependencies:
      <pre><code>pip install -r requirements.txt
      </code></pre>
    </li>
    <li>
      Start the FastAPI server:
      <pre><code>uvicorn app.main:app --reload
      </code></pre>
    </li>
  </ol>
</section>





</body>

