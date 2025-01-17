import requests

def get_gas_fee(gas_price_gwei, gas_limit):
    """
    Calculate the transaction fee in ETH and USD.

    Parameters:
    gas_price_gwei (float): Gas price in Gwei
    gas_limit (int): Gas limit

    Returns:
    dict: Transaction fee in ETH and USD
    """
    eth_price = get_eth_price()  # Fetch current ETH price in USD
    gas_price_eth = gas_price_gwei / 1e9  # Convert Gwei to ETH
    fee_eth = gas_price_eth * gas_limit
    fee_usd = fee_eth * eth_price
    return {
        "fee_eth": fee_eth,
        "fee_usd": fee_usd
    }

def get_eth_price():
    """
    Fetch the current price of Ethereum in USD from CoinGecko API.

    Returns:
    float: Ethereum price in USD
    """
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["ethereum"]["usd"]
    except Exception as e:
        print(f"Error fetching ETH price: {e}")
        return 0.0

if __name__ == "__main__":
    print("=== Ethereum Gas Fee Calculator ===")
    try:
        gas_price_gwei = float(input("Enter Gas Price (in Gwei): "))
        gas_limit = int(input("Enter Gas Limit: "))
        result = get_gas_fee(gas_price_gwei, gas_limit)
        print(f"\nTransaction Fee:")
        print(f"- {result['fee_eth']:.6f} ETH")
        print(f"- ${result['fee_usd']:.2f} USD")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
