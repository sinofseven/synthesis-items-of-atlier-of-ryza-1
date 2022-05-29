import json
from sys import argv
from os.path import basename
from p10_check_type import convert_dataclass, TmpCreatedItem

data = json.load(open('p14_parse.py.json'))
result = set()

for x in data:
    item = convert_dataclass(x)
    for effect in item.effects_in_frame:
        result.add(effect)

json.dump(list(sorted(result)), open(f'{basename(argv[0])}.json', 'w'), indent=2, ensure_ascii=False)
