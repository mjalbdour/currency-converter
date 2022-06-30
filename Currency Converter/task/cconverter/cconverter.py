
import requests
import json

MSG_INPUT_CONICOINS = "Please, enter the number of conicoins you have:"
MSG_INPUT_EXCHANGE_RATE = "Please, enter the exchange rate:"
MSG_OUTPUT_DOLLARS = "The total amount of dollars:"
MSG_OUTPUT_CURRENCY_1 = "I will get"
MSG_OUT_CURRENCY_2 = "from the sale of"

url = "http://www.floatrates.com/daily/"


currency = input().lower()
r = requests.get(f'{url}{currency}.json')
r_text_json = json.loads(r.text)
print(r_text_json["usd"])
print(r_text_json["eur"])

