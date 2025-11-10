import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("COINGECKO_API")

coin = input("Enter cryptocurrency (e.g., bitcoin, ethereum, solana): ").lower()

url = f"{BASE_URL}/{coin}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    name = data["name"]
    symbol = data["symbol"].upper()
    price = data["market_data"]["current_price"]["usd"]
    high = data["market_data"]["high_24h"]["usd"]
    low = data["market_data"]["low_24h"]["usd"]
    change = data["market_data"]["price_change_percentage_24h"]

    print(f"\n--- {name} ({symbol}) ---")
    print(f"Current Price : ${price}")
    print(f"24h High      : ${high}")
    print(f"24h Low       : ${low}")
    print(f"24h Change    : {change}%")

    if change > 0:
        print("Market Trend  : 📈 Rising")
    elif change < 0:
        print("Market Trend  : 📉 Falling")
    else:
        print("Market Trend  : Stable")
else:
    print("Invalid coin name or API error.")