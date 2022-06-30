
from requests import get
from json import loads

MSG_OUTPUT_CHECKING_CACHE = "Checking the cache..."
MSG_OUTPUT_IN_CACHE = "Oh! It is in the cache!"
MSG_OUTPUT_NOT_IN_CACHE = "Sorry, but it is not in the cache!"
MSG_OUTPUT_RECEIVED = "You received"

url = "http://www.floatrates.com/daily/"

currency_cache = {}

currency = input().strip().lower()
with get(f'{url}{currency}.json') as r:
    r_dict = loads(r.text)
    if currency == "usd":
        currency_cache["usd"] = 1
        currency_cache["eur"] = r_dict["eur"]["rate"]
    elif currency == "eur":
        currency_cache["eur"] = 1
        currency_cache["usd"] = r_dict["usd"]["rate"]
    else:
        currency_cache["usd"] = r_dict["usd"]["rate"]
        currency_cache["eur"] = r_dict["eur"]["rate"]

while True:
    currency_to = input().strip().lower()
    if currency_to == "":
        break

    amount = float(input())
    result = 0
    print(MSG_OUTPUT_CHECKING_CACHE)
    if currency_to in currency_cache:
        print(MSG_OUTPUT_IN_CACHE)
    else:
        print(MSG_OUTPUT_NOT_IN_CACHE)
        with get(f'{url}{currency}.json') as r:
            r_dict = loads(r.text)
            currency_cache[currency_to] = r_dict[currency_to]["rate"]

    result = round(amount * currency_cache[currency_to], 2)
    print(f'{MSG_OUTPUT_RECEIVED} {result} {currency_to.upper()}.')
