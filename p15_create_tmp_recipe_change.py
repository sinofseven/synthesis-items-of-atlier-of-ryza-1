import json
from sys import argv
from os.path import basename
from p10_check_type import convert_dataclass, TmpCreatedItem
from typing import List, Optional


data: List[TmpCreatedItem] = [convert_dataclass(x) for x in json.load(open('p14_parse.py.json'))]

result = {}
for item in data:
    for next_recipe in item.changed_recipes:
        node = result.get(next_recipe, {})
        node[item.name] = ''
        result[next_recipe] = node

json.dump(result, open(f'{basename(argv[0])}.json', 'w'), indent=2, ensure_ascii=False)
