cash_conversion = ['rands', 'dollars', 'pounds', 'euros']

cash_conv_from  = input(f'Choose from {cash_conversion}: ')
cash_conv_to = input(f'Choose from {cash_conversion}: ')

cash_currecy = {

}

cash_symbols = {

}

def cash_conversions (amount, currency_from, currency_to):
    cash_converted = cash_currecy.get((currency_from, currency_to))
    

    if cash_converted is None:
        print('Invalid conversion!')
        return None
    return amount * cash_converted

amount = float(input('Enter amount: '))
cash_conv = cash_conversions(amount, cash_conv_from, cash_conv_to)
if cash_conv is not None:
    cash_sign_1 = cash_currecy[cash_symbols]
    cash_sign_2 = cash_currecy[cash_symbols]
    print (f'{cash_sign_1} {amount} = {cash_sign_2} {cash_conv}')

#forex-python pip

from forex_python import CurrencyRates
cr = CurrencyRates

cash_conversion = ('usd', 'eur', 'zar')
amount = float(input('Enter amount: '))
cash_conv_from  = input(f'Choose from {cash_conversion}: ')
cash_conv_to = input(f'Choose from {cash_conversion}: ')

converted_amount = cr.convert(cash_conv_from, cash_conv_to, amount)
print(f'{amount} {cash_conv_from} = {amount} {cash_conv_to}')