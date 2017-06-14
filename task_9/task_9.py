import json
import re
import sys
import codecs
import chardet


def get_text_from_item(an_item):
    try:
        line = an_item['description']['__cdata']
    except TypeError:
        line = an_item['description']
    line = re.sub(r'(<.*?>)*(/.*/)*', '', line).rstrip()
    return line


def get_dict_from_text(text):
    word_list = text.split()
    d = dict((word, word_list.count(word)) for word in word_list if len(word) >= 6)
    return d


def get_file_encoding(filename):
    with open(filename, 'rb') as f:
        return chardet.detect(f.read())['encoding']


def main():
    sys.stdout = codecs.getwriter('UTF-8')(sys.stdout.buffer, 'strict')
    filename = input('Введите имя файла: ')
    enc = get_file_encoding(filename)
    with open(filename, encoding=enc) as f:
        content = json.load(f)
        items_list = content['rss']['channel']['item']
        global_dict = dict()
        for an_item in items_list:
            text = get_text_from_item(an_item)
            current_dict = get_dict_from_text(text)
            for a_word, word_count in current_dict.items():
                if a_word in global_dict.keys():
                    global_dict[a_word] += word_count
                else:
                    global_dict[a_word] = word_count
        d = sorted(global_dict.items(), key=lambda x: x[1], reverse=True)
        for i in range(10):
            print('{} {}'.format(d[i][0], d[i][1]))


main()
