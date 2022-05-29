import json
from sys import argv
from os.path import basename
from dataclasses import dataclass, asdict


@dataclass()
class Mapping:
    base_recipe: str
    need_item: str
    next_recipe: str


data = [Mapping(**x) for x in json.load(open('02_convert_dict.py.json'))]

print(len(data), len(set([x.next_recipe for x in data])))

result = {}
for item in data:
    node = result.get(item.next_recipe, {})
    node[item.base_recipe] = item.need_item
    result[item.next_recipe] = node

json.dump(result, open(f'{basename(argv[0])}.json', 'w'), indent=2, ensure_ascii=False, default=asdict)
