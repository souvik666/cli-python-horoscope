import requests

def getSigns():
    return requests.get("http://sandipbgt.com/theastrologer/api/sunsigns/",).json() ## fetching signs
def getHoroscope(sign, timeframe):
    return requests.get(f"http://sandipbgt.com/theastrologer/api/horoscope/{sign}/{timeframe}",).json()
    ##fetching horoscope with user input