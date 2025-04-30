import os
import yaml
import requests

def load_config():
    base_path = os.path.dirname(__file__)
    config_path = os.path.join(base_path, "config", "config.yaml")
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

def fetch_crypto_data():
    config = load_config()
    
    # Get parameters from config
    try:
        params = config["crypto_params"]
        url = config["coingecko_url"]
    except KeyError as e:
        print(f"Missing key in config.yaml: {e}")
        return

    # Send request to API
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        print("Error fetching data:", response.status_code)
        print("Response text:", response.text)
        return

    try:
        data = response.json()
    except Exception as e:
        print("Failed to parse JSON response")
        print("Raw response text:", response.text)
        print("Error:", e)
        return

    # Check format and print results
    if isinstance(data, list):
        print("CoinGecko Market Data:")
        for coin in data:
            print(f"{coin['id'].capitalize()}: ${coin['current_price']}")
    else:
        print("Unexpected data format:", type(data), data)
    
def fetch_binance_data():
    import requests
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url)
    data = response.json()
    print("DEBUG Binance response:", data)

    if 'price' in data:
        print(f"Binance BTC/USDT Price: ${data['price']}")
    else:
        print("Price not found in Binance response.")
