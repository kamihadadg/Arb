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


# Wallex '10610|7kKfnHXfZRDEXvN44F5Yl1W31mXYEZp5ucfWqQs7'
def get_price_from_Wallex():
    try:
        url = "https://api.wallex.ir/v1/depth?symbol=USDTTMN"
        headers = {
            'X-API-Key': '10610|7kKfnHXfZRDEXvN44F5Yl1W31mXYEZp5ucfWqQs7'
        }
        
        response = requests.get(url ,headers=headers)
        response.raise_for_status()
        price_data = response.json()
        
        # return(price_data)
        
        # گرفتن آخرین معامله از لیست latestTrades
        bidprice= price_data['result']['ask'][0]['price']
        bidqty = price_data['result']['ask'][0]['quantity']
        askprice = price_data['result']['bid'][0]['price']
        askqty = price_data['result']['bid'][0]['quantity']
        
        return {"Wallex askP": askprice,"Wallex askqty":askqty,"Wallex bid": bidprice,"Wallex bidqty": bidqty}
    
    except requests.RequestException as e:
        return {"Wallex": f"Error fetching price: {str(e)}"}

# Wallex '10610|7kKfnHXfZRDEXvN44F5Yl1W31mXYEZp5ucfWqQs7'
def get_price_from_Nobitex():
    try:
        url = "https://api.nobitex.ir/v2/orderbook/USDTIRT"
        # headers = {
        #     'X-API-Key': '10610|7kKfnHXfZRDEXvN44F5Yl1W31mXYEZp5ucfWqQs7'
        # }
        
        response = requests.get(url)
        response.raise_for_status()
        price_data = response.json()
        
        # گرفتن آخرین معامله از لیست latestTrades
        askprice = float(price_data['asks'][0][0])
        askqty = float(price_data['asks'][0][1])
        bidprice = float(price_data['bids'][0][0])
        bidqty = float(price_data['bids'][0][1])

        
        return {"Nobitex askP": askprice/10,"Nobitex askqty":askqty,"Nobitex bid": bidprice/10,"Nobitex bidqty": bidqty}
    
    except requests.RequestException as e:
        return {"Nobitex": f"Error fetching price: {str(e)}"}


@app.route('/prices', methods=['GET'])
def get_prices():
    prices = {}

    # try:
    #     prices.update(get_price_from_binance())
    # except Exception:
    #     prices["Binance"] = "Error fetching price"
    
    # try:
    #     prices.update(get_price_from_huobi())
    # except Exception:
    #     prices["Huobi"] = "Error fetching price"
    
    # try:
    #     prices.update(get_price_from_kraken())
    # except Exception:
    #     prices["Kraken"] = "Error fetching price"
    

    # try:
    #     prices.update(get_price_from_bitfinex())
    # except Exception:
    #     prices["Bitfinex"] = "Error fetching price"
    
    # try:
    #     prices.update(get_price_from_coinbase_pro())
    # except Exception:
    #     prices["Coinbase Pro"] = "Error fetching price"
    
    # try:
    #     prices.update(get_price_from_gate_io())
    # except Exception:
    #     prices["Gate.io"] = "Error fetching price"
    # try:
    #     prices.update(get_price_from_okx())
    # except Exception:
    #     prices["OKX"] = "Error fetching price"   
    # try:
    #     prices.update(get_price_from_bybit())
    # except Exception:
    #     prices["bybit"] = "Error fetching price" 
    try:
        prices.update(get_price_from_Wallex())
    except Exception:
        prices["Wallex"] = "Error fetching price" 
    try:
        prices.update(get_price_from_Nobitex())
    except Exception:
        prices["Nobitex"] = "Error fetching price"  
    
    
    nbid=prices["Nobitex bid"]
    Waskp=prices["Wallex askP"]
    Percent=(100*(nbid-Waskp)/(nbid if nbid > Waskp else Waskp))
    MyComm=abs(nbid-Waskp)-0.0035*(nbid+Waskp)
    Commition=0.0035*(nbid+Waskp)
    Deal=('Deal ",'if (abs(nbid-Waskp)-0.0035*(nbid+Waskp)>0) else "No Deal")
    Buyfrom=("Nobitext" if nbid < Waskp else "Wallex")
    Sellfrom=("Nobitext" if nbid > Waskp else "Wallex")
    
    return jsonify(
                   
                   {
                       
                    "Nbid":nbid,
                    "Wask":Waskp,
                   },
                       
                   {    
                    "Percent":Percent,
                    "MyComm":MyComm,
                    "Commition":Commition,
                    
                   },
                   {
                    "Deal":Deal,
                    "Buyfrom":Buyfrom,
                    "Sellfrom":Sellfrom,
                    },
                  
                   
                   )
    # return jsonify({
    #                     'Naskp':prices["Nobitex askP"],
    #                     'Waskp':prices["Wallex askP"],
    #                     'Nbidp':prices["Nobitex askqty"],
    #                     'Wbidp':prices["Wallex askqty"],
    #                     'Naskq':prices["Nobitex bid"],
    #                     'Waskq':prices["Wallex bid"],
    #                     'Nbidq':prices["Nobitex bidqty"],
    #                     'Wbidq':prices["Wallex bidqty"],
    #                 })
    

if __name__ == '__main__':
    app.run(debug=True)
