
MSG_INPUT_CONICOINS = "Please, enter the number of conicoins you have:"
MSG_INPUT_EXCHANGE_RATE = "Please, enter the exchange rate:"
MSG_OUTPUT_DOLLARS = "The total amount of dollars:"
MSG_OUTPUT_CURRENCY_1 = "I will get"
MSG_OUT_CURRENCY_2 = "from the sale of"

conicoin_to_currency = {
    "RUB": 2.98,
    "ARS": 0.82,
    "HNL": 0.17,
    "AUD": 1.9622,
    "MAD": 0.208
}


def conicoin_to_dollar(amount, exchange_r):
    return round(amount * exchange_r, 2)


conicoins = float(input())
for currency, exchange_rate in conicoin_to_currency.items():
    result = conicoin_to_dollar(conicoins, exchange_rate)
    print(f'{MSG_OUTPUT_CURRENCY_1} {result} {currency} {MSG_OUT_CURRENCY_2} {conicoins} conicoins.')
