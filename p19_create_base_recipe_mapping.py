import json
from typing import Dict
from sys import argv
from os.path import basename


data: Dict[str, Dict[str, str]] = json.load(open('p18_next_recipe_mapping.json'))

result = {}
for base_recipe, v in data.items():
    for next_recipe, need_item in v.items():
        node = result.get(next_recipe, {})
        node[base_recipe] = need_item
        result[next_recipe] = node

json.dump(result, open(f'{basename(argv[0])}.json', 'w'), indent=2, ensure_ascii=False)
