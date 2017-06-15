import osa

URL = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'

def get_prices_and_currencies(filename):
  out = []
  with open(filename) as f:
    while True:
      l = f.readline()
      if not l:
        break
      else:
        data = l.split()
        out.append([float(data[1]), data[2]])
  return out


def get_total_in_rubles(flight_list):
  client1 = osa.client.Client(URL)
  total_cost = 0.
  for cost, currency in flight_list:
   total_cost += client1.service.ConvertToNum(fromCurrency = currency, toCurrency = 'RUB', amount = cost, rounding = True)
  return total_cost

def main():
  filename = input('Enter filename: ')
  flight_list = get_prices_and_currencies(filename)
  print('{0:.2f}'.format(get_total_in_rubles(flight_list)))

main()
