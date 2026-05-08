# Binance Futures Trading Bot

A simple Python trading bot for Binance Futures Demo/Testnet using REST API and Streamlit UI.

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- Streamlit UI
- CLI support
- Input validation
- Logging support
- REST API integration

---

## Project Structure

```bash
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── cli.py
├── ui.py
├── README.md
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/MICK-AI/binance-trading-bot.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## API Setup

1. Go to Binance Futures Demo/Testnet
2. Generate API Key and Secret Key
3. Add keys inside `client.py`

---

## Run Streamlit UI

```bash
streamlit run ui.py
```

---

## Run CLI

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --quantity 0.001
```

---

## Technologies Used

- Python
- Requests
- Streamlit
- Binance Futures REST API

---

## Assumptions

- User has valid Binance Demo/Testnet API credentials
- Demo/Testnet environment is active
- Internet connection is available