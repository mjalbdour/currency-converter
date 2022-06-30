
MSG_INPUT_CONICOINS = "Please, enter the number of conicoins you have:"
MSG_INPUT_EXCHANGE_RATE = "Please, enter the exchange rate:"
MSG_OUTPUT_DOLLARS = "The total amount of dollars:"


def conicoin_to_dollar(amount, exchange_r):
    return amount * exchange_r


print(MSG_INPUT_CONICOINS)
conicoins = int(input())
print(MSG_INPUT_EXCHANGE_RATE)
exchange_rate = float(input())
result = conicoin_to_dollar(conicoins, exchange_rate)
print(f'{MSG_OUTPUT_DOLLARS} {result}')
