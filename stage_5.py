import requests 
input = input().lower() 
url = print(f'http://www.floatrates.com/daily/{input}.json') 
r = requests.get(url).json() 
dct = {} 
if input != 'usd': 
    dct['usd'] = str(r['usd']) 
if input != 'eur': 
    dct['eur'] = str(r['eur']) 
print(dct['usd']) 
print(dct['eur'])