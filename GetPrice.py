from flask import Flask, jsonify
import requests

app = Flask(__name__)

def get_price_from_binance():
    try:
        response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT")
        response.raise_for_status()
        price_data = response.json()
        return {"Binance": price_data['price']}
    except requests.RequestException:
        return {"Binance": "Error fetching price"}

def get_price_from_huobi():
    try:
        response = requests.get("https://api.huobi.pro/market/detail/merged?symbol=xrpusdt")
        response.raise_for_status()
        price_data = response.json()
        return {"Huobi": price_data['tick']['close']}
    except requests.RequestException:
        return {"Huobi": "Error fetching price"}

def get_price_from_kraken():
    try:
        response = requests.get("https://api.kraken.com/0/public/Ticker?pair=XRPUSD")
        response.raise_for_status()
        price_data = response.json()
        return {"Kraken": price_data['result']['XXRPZUSD']['c'][0]}
    except requests.RequestException:
        return {"Kraken": "Error fetching price"}



def get_price_from_bitfinex():
    try:
        response = requests.get("https://api.bitfinex.com/v1/pubticker/xrpusd")
        response.raise_for_status()
        price_data = response.json()
        return {"Bitfinex": price_data['last_price']}
    except requests.RequestException:
        return {"Bitfinex": "Error fetching price"}

def get_price_from_coinbase_pro():
    try:
        response = requests.get("https://api.pro.coinbase.com/products/XRP-USD/ticker")
        response.raise_for_status()
        price_data = response.json()
        return {"Coinbase Pro": price_data['price']}
    except requests.RequestException:
        return {"Coinbase Pro": "Error fetching price"}

def get_price_from_gate_io():
    try:
        response = requests.get("https://api.gateio.ws/api/v4/spot/tickers?currency_pair=XRP_USDT")
        response.raise_for_status()
        price_data = response.json()
        return {"Gate.io": price_data[0]['last']}
    except requests.RequestException:
        return {"Gate.io": "Error fetching price"}
def get_price_from_okx():
    try:
        response = requests.get("https://www.okx.com/api/v5/market/ticker?instId=XRP-USDT")
        response.raise_for_status()
        price_data = response.json()
        return {"OKX": price_data['data'][0]['last']}
    except requests.RequestException:
        return {"OKX": "Error fetching price"}
    
def get_price_from_bybit():
    try:
        response = requests.get("https://api.bybit.com/v2/public/tickers?symbol=XRPUSDT")
        response.raise_for_status()
        price_data = response.json()
        return {"Bybit": price_data['result'][0]['last_price']}
    except requests.RequestException:
        return {"Bybit": "Error fetching price"}

@app.route('/prices', methods=['GET'])
def get_prices():
    prices = {}

    # try:
    #     prices.update(get_price_from_binance())
    # except Exception:
    #     prices["Binance"] = "Error fetching price"
    
    try:
        prices.update(get_price_from_huobi())
    except Exception:
        prices["Huobi"] = "Error fetching price"
    
    try:
        prices.update(get_price_from_kraken())
    except Exception:
        prices["Kraken"] = "Error fetching price"
    

    try:
        prices.update(get_price_from_bitfinex())
    except Exception:
        prices["Bitfinex"] = "Error fetching price"
    
    try:
        prices.update(get_price_from_coinbase_pro())
    except Exception:
        prices["Coinbase Pro"] = "Error fetching price"
    
    try:
        prices.update(get_price_from_gate_io())
    except Exception:
        prices["Gate.io"] = "Error fetching price"
    try:
        prices.update(get_price_from_okx())
    except Exception:
        prices["OKX"] = "Error fetching price"   
    try:
        prices.update(get_price_from_bybit())
    except Exception:
        prices["bybit"] = "Error fetching price" 
    return jsonify(prices)

if __name__ == '__main__':
    app.run(debug=True)
