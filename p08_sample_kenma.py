import json
from sys import argv
from os.path import basename


data = [x for x in open('03_list_creatable_items.txt').read().split('\n') if x][4]

json.dump([x for x in data.split('|') if x], open(f'{basename(argv[0])}.json', 'w'), indent=2, ensure_ascii=False)
