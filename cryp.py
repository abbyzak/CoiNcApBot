import requests

# CoinMarketCap API endpoint
API_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

# Replace 'YOUR_API_KEY' with your actual CoinMarketCap API key
API_KEY = 'xx'

# Coin to track
coin_symbol = 'BTC'

# Time intervals for percentage change calculation (in minutes)

# Time intervals for percentage change calculation
time_intervals = ['1h', '24h', '7d']

# Make API request to CoinMarketCap
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY
}

params = {
    'symbol': coin_symbol
}

response = requests.get(API_URL, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    coin_data = data['data'][coin_symbol]

    # Get the current price
    current_price = coin_data['quote']['USD']['price']

    # Calculate percentage change for each time interval
    for interval in time_intervals:
        historical_price = coin_data['quote']['USD']['percent_change_' + interval]
        percentage_change = historical_price
        print(f'Percentage Change in {interval}: {percentage_change:.2f}%')

else:
    print(f'Error: {response.status_code} - {response.text}')
