import json
from sys import argv
from os.path import basename


data = json.load(open('00_base.json'))

previous = None
for i, (a, b, c) in enumerate(data):
    if a == '':
        data[i] = [previous, b, c]
    else:
        previous = a

json.dump(data, open(f'{basename(argv[0])}.json', 'w'), indent=2, ensure_ascii=False)
