def parse_cook_book_file(filename):
  cook_book = {}
  with open(filename, encoding = 'UTF-8') as f:
    while True:
      line = f.readline()
      if not line:
        break
      if line == '\n':
        continue
      else:
        dish_name = line.lower().rstrip('\n')
        ingridients_count = int(f.readline().rstrip('\n'))
        ingridients_list = []
        for _ in range(ingridients_count):
          ingridient_line = f.readline().rstrip('\n')
          ingridient_dict = parse_ingridient_line(ingridient_line)
          ingridients_list.append(ingridient_dict)
        cook_book[dish_name] = ingridients_list
  return cook_book

def parse_ingridient_line(ingridient_line):
  parsed_line = dict()
  raw_list = ingridient_line.split(' | ')
  parsed_line['ingridient_name'] = raw_list[0].lower()
  parsed_line['quantity'] = int(raw_list[1])
  parsed_line['measure'] = raw_list[2].lower()
  return parsed_line

def get_shop_list_by_dishes(dishes, person_count, cook_book):
      shop_list = {}
      for dish in dishes:
        for ingridient in cook_book[dish]:
          new_shop_list_item = dict(ingridient)

          new_shop_list_item['quantity'] *= person_count
          if new_shop_list_item['ingridient_name'] not in shop_list:
            shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
          else:
            shop_list[new_shop_list_item['ingridient_name']]['quantity'] += \
              new_shop_list_item['quantity']
      return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], 
                            shop_list_item['measure']))

def create_shop_list():
  cook_book_filename = input('Введите имя файла с книгой рецептов: ')
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  cook_book = parse_cook_book_file(cook_book_filename)
  shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
  print_shop_list(shop_list)

create_shop_list()