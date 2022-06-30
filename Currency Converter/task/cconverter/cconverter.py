
def conicoin_to_dollar(amount):
    return amount * 100


conicoins = int(input())
print(f'I have {conicoins} conicoins.')
print(f'{conicoins} conicoins cost {conicoin_to_dollar(conicoins)} dollars.')
print('I am rich! Yippee!')
