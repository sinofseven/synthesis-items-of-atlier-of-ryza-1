import json
from dataclasses import dataclass, asdict
import re
from typing import List, Optional
from sys import argv
from os.path import basename


@dataclass()
class InjectedNumbers:
    max: int
    min: int


@dataclass()
class Elements:
    type: List[str]
    min: int
    max: int


@dataclass()
class CreatedItem:
    name: str
    level: int
    category: List[str]
    created_numbers: int
    injected_numbers: InjectedNumbers
    elementals: Elements
    source_items: List[str]
    effects_in_frame: List[str]
    effects_not_in_frame: List[str]
    changed_recipes: List[str]


def express(obj):
    print(json.dumps(obj, indent=2, ensure_ascii=False, default=asdict))


def parse_wiki_page(text: str) -> List[str]:
    return re.findall(r'\[\[(.*)>', text)


def parse_name(line: str) -> str:
    result = parse_wiki_page(line)
    return result[0]


def parse_level(line: str) -> int:
    return int(line.replace('個', ''))


def parse_category(line: str) -> List[str]:
    return line.split('&br;')


def parse_created_numbers(line: str) -> int:
    return int(line.replace('個', ''))


def parse_injected_numbers(line1: str, line2: str) -> InjectedNumbers:
    result = InjectedNumbers(
        max=int(line1.replace('回', '')),
        min=int(line2.replace('回', ''))
    )
    return result


def parse_elementals(line: str) -> Elements:
    num_min = int(line[-3])
    num_max = int(line[-1])
    elements = [x for x in line[:-3]]
    return Elements(
        min=num_min,
        max=num_max,
        type=elements
    )


def parse_source_items(line: str) -> List[str]:
    return line.split('&br;')


def parse_effects_in_frame(line: str) -> List[str]:
    return [x[4:] for x in line.split('&br;')]


def parse_effects_not_in_frame(line: str) -> List[str]:
    return line.split('&br;')


def parse_changed_recipes(line: str) -> List[str]:
    if line == '-':
        return []
    return [parse_wiki_page(x)[0] for x in line.split('&br;')]


def parse(line: str) -> CreatedItem:
    part = [x for x in line.split('|') if x]
    if len(part) == 10:
        part.append('-')
    return CreatedItem(
        name=parse_name(part[0]),
        level=parse_level(part[1]),
        category=parse_category(part[2]),
        created_numbers=parse_created_numbers(part[3]),
        injected_numbers=parse_injected_numbers(part[4], part[5]),
        elementals=parse_elementals(part[6]),
        source_items=parse_source_items(part[7]),
        effects_in_frame=parse_effects_in_frame(part[8]),
        effects_not_in_frame=parse_effects_not_in_frame(part[9]),
        changed_recipes=parse_changed_recipes(part[10])
    )


def main():
    raw = [x for x in open('03_list_creatable_items.txt').read().split('\n') if x]
    result = [parse(line) for line in raw]
    json.dump(result, open(f'{basename(argv[0])}.json', 'w'), indent=2, ensure_ascii=False, default=asdict)


if __name__ == '__main__':
    main()
