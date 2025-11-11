import requests

product_name = input("Enter product name: ")
target_currency = input("Convert price to currency (INR/EUR/JPY): ").upper()

# --- API 1: FakeStore Products ---
products_url = "https://fakestoreapi.com/products"
products = requests.get(products_url).json()

product = None
for item in products:
    if product_name.lower() in item["title"].lower():
        product = item
        break

if not product:
    print("Product not found!")
    exit()

usd_price = product["price"]
print(f"\nFound Product: {product['title']}")
print(f"Base Price: ${usd_price}")

# --- API 2: Currency Conversion ---
rate_url = f"https://api.exchangerate-api.com/v4/latest/USD"
rates = requests.get(rate_url).json()
conversion_rate = rates["rates"].get(target_currency)

if not conversion_rate:
    print("Invalid currency!")
    exit()

converted_price = usd_price * conversion_rate

print(f"\nConverted Price in {target_currency}: {converted_price:.2f}")
print(f"Exchange Rate: 1 USD = {conversion_rate} {target_currency}")