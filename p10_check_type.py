from dataclasses import dataclass, asdict
from typing import List, Union
import json


@dataclass()
class TmpInjectedNumbers:
    max: int
    min: int


@dataclass()
class TmpElements:
    type: List[str]
    min: int
    max: int


@dataclass()
class TmpCreatedItem:
    name: str
    level: int
    category: List[str]
    created_numbers: int
    injected_numbers: TmpInjectedNumbers
    elementals: TmpElements
    source_items: List[str]
    effects_in_frame: List[str]
    effects_not_in_frame: List[str]
    changed_recipes: List[str]


def convert_dataclass(data: dict) -> TmpCreatedItem:
    def convert_value(key, value):
        if key == 'injected_numbers':
            return TmpInjectedNumbers(**value)
        elif key == 'elementals':
            return TmpElements(**value)
        else:
            return value

    return TmpCreatedItem(**{
        k: convert_value(k, v)
        for k, v in data.items()
    })


def main():
    data = json.load(open('07_test_parse.py.json'))
    for i, item in enumerate(data):
        try:
            convert_dataclass(item)
        except Exception as e:
            print(i, e)


if __name__ == '__main__':
    main()
