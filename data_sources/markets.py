import yfinance as yf

def fetch_markets():
    tickers = {
        "S&P 500": "^GSPC",
        "VIX": "^VIX",
        "Bitcoin (USD)": "BTC-USD",
        "Ethereum (USD)": "ETH-USD",
        "iShares Gold (IAU)": "IAU",
    }

    results = {}

    for label, symbol in tickers.items():
        try:
            ticker = yf.Ticker(symbol)
            data = ticker.history(period="2d")   # need at least two days for prev close

            if data.empty or len(data) < 2:
                results[label] = {"price": "N/A", "change": "N/A", "pct": "N/A"}
                continue

            latest = float(data["Close"].iloc[-1])
            prev = float(data["Close"].iloc[-2])
            diff = round(latest - prev, 2)
            pct = round((diff / prev) * 100, 2)

            results[label] = {
                "price": round(latest, 2),
                "change": diff,
                "pct": pct
            }

        except Exception:
            results[label] = {"price": "N/A", "change": "N/A", "pct": "N/A"}

    return results

if __name__ == "__main__":
    import pprint
    pprint.pprint(fetch_markets())
