import json
from dataclasses import dataclass, asdict
from sys import argv
from os.path import basename


@dataclass()
class Node:
    base_recipe: str
    need_item: str
    next_recipe: str


data = json.load(open('01_add_base_name.py.json'))
result = [
    Node(*x) for x in data
]

json.dump(result, open(f'{basename(argv[0])}.json', 'w'), indent=2, ensure_ascii=False, default=asdict)
