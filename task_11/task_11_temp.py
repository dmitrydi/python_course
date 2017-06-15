import osa
import re

URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'

def get_temperatures_from_file(filename):
  with open(filename) as f:
    string = f.read()
    return re.findall(r'[0-9]+', string)

def get_average_temp_in_celsius(temperatures_in_f):
  client1 = osa.client.Client(URL)
  t_c = 0.0
  for t_f in temperatures_in_f:
    t_c += client1.service.ConvertTemp(Temperature = float(t_f), FromUnit = "degreeFahrenheit", ToUnit = "degreeCelsius")
  return t_c/len(temperatures_in_f)

def main():
  filename = input('Enter filename: ')
  ts_in_f = get_temperatures_from_file(filename)
  print('{0:.2f}'.format(get_average_temp_in_celsius(ts_in_f)))

main()

