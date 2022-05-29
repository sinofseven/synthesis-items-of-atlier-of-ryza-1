import json
from typing import List
from sys import argv
from os.path import basename


data: List[str] = json.load(open('p21_parse_effects_in_frame.py.json'))
result = [
    x for x in data
    if x.find('付与') >= 0
]

json.dump(result, open(f'{basename(argv[0])}.json', 'w'), indent=2, ensure_ascii=False)
