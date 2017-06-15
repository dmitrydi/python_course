import osa

URL = 'http://www.webservicex.net/length.asmx?WSDL'

def parse_file(filename):
  out = []
  with open(filename) as f:
    while True:
      l = f.readline()
      if not l:
        break
      else:
        data = l.split()
        out.append(float(data[1].replace(',','')))
  return out


def get_total_distance(distances_in_miles):
  client1 = osa.client.Client(URL)
  total_distance = 0.
  for d in distances_in_miles:
   total_distance += client1.service.ChangeLengthUnit(LengthValue = d, fromLengthUnit = 'Miles', toLengthUnit = 'Kilometers')
  return total_distance

def main():
  filename = input('Enter filename: ')
  distances_in_miles = parse_file(filename)
  print(distances_in_miles)
  print('{0:.2f}'.format(get_total_distance(distances_in_miles)))

main()
