from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Define functions to get prices for each cryptocurrency

def get_price_from_binance(symbol):
    try:
        response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")
        response.raise_for_status()
        price_data = response.json()
        return {symbol: price_data['price']}
    except requests.RequestException:
        return {symbol: "Error fetching price"}

def get_price_from_huobi(symbol):
    try:
        response = requests.get(f"https://api.huobi.pro/market/detail/merged?symbol={symbol}")
        response.raise_for_status()
        price_data = response.json()
        return {symbol: price_data['tick']['close']}
    except requests.RequestException:
        return {symbol: "Error fetching price"}

def get_price_from_kraken(symbol):
    try:
        response = requests.get(f"https://api.kraken.com/0/public/Ticker?pair={symbol}")
        response.raise_for_status()
        price_data = response.json()
        return {symbol: price_data['result'][list(price_data['result'].keys())[0]]['c'][0]}
    except requests.RequestException:
        return {symbol: "Error fetching price"}

def get_price_from_kucoin(symbol):
    try:
        response = requests.get(f"https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={symbol}")
        response.raise_for_status()
        price_data = response.json()
        return {symbol: price_data['data']['price']}
    except requests.RequestException:
        return {symbol: "Error fetching price"}

def get_price_from_lbank(symbol):
    try:
        response = requests.get(f"https://api.lbank.info/v2/ticker.do?symbol={symbol}")
        response.raise_for_status()
        price_data = response.json()
        return {symbol: price_data['ticker']['latest']}
    except requests.RequestException:
        return {symbol: "Error fetching price"}

def get_price_from_bitfinex(symbol):
    try:
        response = requests.get(f"https://api.bitfinex.com/v1/pubticker/{symbol}")
        response.raise_for_status()
        price_data = response.json()
        return {symbol: price_data['last_price']}
    except requests.RequestException:
        return {symbol: "Error fetching price"}

def get_price_from_coinbase_pro(symbol):
    try:
        response = requests.get(f"https://api.pro.coinbase.com/products/{symbol}/ticker")
        response.raise_for_status()
        price_data = response.json()
        return {symbol: price_data['price']}
    except requests.RequestException:
        return {symbol: "Error fetching price"}

def get_price_from_gate_io(symbol):
    try:
        response = requests.get(f"https://api.gateio.ws/api/v4/spot/tickers?currency_pair={symbol}")
        response.raise_for_status()
        price_data = response.json()
        return {symbol: price_data[0]['last']}
    except requests.RequestException:
        return {symbol: "Error fetching price"}

@app.route('/prices', methods=['GET'])
def get_prices():
    symbols = {
        "BTCUSDT": "Bitcoin",
        "ETHUSDT": "Ethereum",
        "ADAUSDT": "Cardano",
        "XRPUSDT": "Ripple",
        "SOLUSDT": "Solana"
    }

    prices = {}

    for symbol, name in symbols.items():
        try:
            binance_price = get_price_from_binance(symbol)
            prices.update(binance_price)
        except Exception:
            prices[name] = "Error fetching price"
        
        try:
            huobi_price = get_price_from_huobi(symbol)
            prices.update(huobi_price)
        except Exception:
            prices[name] = "Error fetching price"

        try:
            kraken_price = get_price_from_kraken(symbol)
            prices.update(kraken_price)
        except Exception:
            prices[name] = "Error fetching price"

        try:
            kucoin_price = get_price_from_kucoin(symbol)
            prices.update(kucoin_price)
        except Exception:
            prices[name] = "Error fetching price"

        try:
            lbank_price = get_price_from_lbank(symbol)
            prices.update(lbank_price)
        except Exception:
            prices[name] = "Error fetching price"

        try:
            bitfinex_price = get_price_from_bitfinex(symbol)
            prices.update(bitfinex_price)
        except Exception:
            prices[name] = "Error fetching price"

        try:
            coinbase_pro_price = get_price_from_coinbase_pro(symbol)
            prices.update(coinbase_pro_price)
        except Exception:
            prices[name] = "Error fetching price"

        try:
            gate_io_price = get_price_from_gate_io(symbol)
            prices.update(gate_io_price)
        except Exception:
            prices[name] = "Error fetching price"

    return jsonify(prices)

if __name__ == '__main__':
    app.run(debug=True)
