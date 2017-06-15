import requests
import sys
import codecs
import chardet

def translate_it(text, from_lang, to_lang, URL, API_KEY):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param to_lang:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])

def translate_from_file_to_file(in_file, out_file, from_lang, to_lang, URL, API_KEY):
  with open(in_file, encoding = 'UTF-8') as f:
    text = f.read()
  #with open(in_file, 'rb') as f:
  #  print(chardet.detect(f.read()))
  translation = translate_it(text, from_lang, to_lang, URL, API_KEY)
  with open(out_file, 'w', encoding = 'UTF-8') as f:
    f.write(translation)

def main():
  API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
  URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

  sys.stdout = codecs.getwriter('UTF-8')(sys.stdout.buffer, 'strict')
  in_file = input('Введите имя исходного файла: ')
  out_file = input('Введите имя конечного файла: ')
  from_lang = input('Введите язык исходного файла: ')
  to_lang = input('Введите язык перевода: ')
  translate_from_file_to_file(in_file, out_file, from_lang, to_lang, URL, API_KEY)
  print('Перевод успешно выполнен, результат в файле {}'.format(out_file))

main()
