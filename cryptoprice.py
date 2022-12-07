import tweepy
import time
import json
import requests

auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")
api = tweepy.API(auth)
cryptos = ['BTC', 'ETH', 'BNB','XRP', 'DOGE', 'AVAX', 'SOL', 'DOT']
prices = {}
url = 'https://api.binance.com/api/v3/ticker/price?symbol={}USDT'
admin = '2681699286'

def getprices():
    for crypto in cryptos:
        response = requests.get(url.format(crypto))
        if response.status_code == 200:
            price = float(response.json()['price'])
            prices[crypto] = price
    
def tweet():
    getprices()
    status = (f"#BTC Bitcoin ${prices.get('BTC'):,}\n#ETH Ethereum ${prices.get('ETH'):,}\n#BNB BNB ${prices.get('BNB'):,}\n#XRP Ripple ${prices.get('XRP'):,}\n#DOGE Dogecoin ${prices.get('DOGE'):,}")
    api.update_status(status)
def main():
    while True:
        try:
            tweet()
            print("tweeted")
            time.sleep(30 * 60)
        except KeyboardInterrupt:
            api.send_direct_message(admin, "keyboard interrupt")
            break
        except:
            print("some error.")
            api.send_direct_message(admin, "cant tweet")
            pass


if __name__ == "__main__":
    main()
