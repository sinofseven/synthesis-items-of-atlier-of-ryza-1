from sys import argv
from os.path import basename
import json
from dataclasses import dataclass, asdict
from p10_check_type import TmpCreatedItem, convert_dataclass
from typing import List, Dict


@dataclass()
class Categories:
    have: List[str]
    optional: List[str]


@dataclass()
class InjectedNumbers:
    max: int
    min: int


@dataclass()
class Elementals:
    have: List[str]
    optional: List[str]
    max: int
    min: int


@dataclass()
class SynthesisItem:
    name: str
    level: int
    categories: Categories
    createdNumbers: int
    injectedNumbers: InjectedNumbers
    elementals: Elementals
    sourceItems: List[str]
    effectsInFrame: List[str]
    effectsNotInFrame: List[str]
    baseRecipes: Dict[str, str]


def convert_to_injected_numbers(item: TmpCreatedItem) -> InjectedNumbers:
    return InjectedNumbers(
        max=item.injected_numbers.max,
        min=item.injected_numbers.min
    )


def convert_to_categories(item: TmpCreatedItem) -> Categories:
    return Categories(
        have=item.category,
        optional=[
            x[:-2] for x in item.effects_in_frame
            if x.find(')付与') > 0
        ]
    )


def convert_to_elements(item: TmpCreatedItem) -> Elementals:
    return Elementals(
        max=item.elementals.max,
        min=item.elementals.min,
        have=item.elementals.type,
        optional=[
            x[0] for x in item.effects_in_frame
            if x.find('属性付与') > 0
        ]
    )


def convert_to_base_recipes(item: TmpCreatedItem, mapping: Dict[str, Dict[str, str]]) -> Dict[str, str]:
    return mapping.get(item.name, {})


def convert(tmp_item: TmpCreatedItem, base_recipe_mapping: Dict[str, Dict[str, str]]) -> SynthesisItem:
    return SynthesisItem(
        name=tmp_item.name,
        level=tmp_item.level,
        categories=convert_to_categories(tmp_item),
        createdNumbers=tmp_item.created_numbers,
        injectedNumbers=convert_to_injected_numbers(tmp_item),
        elementals=convert_to_elements(tmp_item),
        sourceItems=tmp_item.source_items,
        effectsInFrame=tmp_item.effects_in_frame,
        effectsNotInFrame=tmp_item.effects_not_in_frame,
        baseRecipes=convert_to_base_recipes(tmp_item, base_recipe_mapping)
    )


def main():
    tmp_items = [convert_dataclass(x) for x in json.load(open('p14_parse.py.json'))]
    base_recipe_mapping = json.load(open('p19_create_base_recipe_mapping.py.json'))
    result = [
        convert(x, base_recipe_mapping)
        for x in tmp_items
    ]
    json.dump(result, open(f'{basename(argv[0])}.json', 'w'), indent=2, ensure_ascii=False, default=asdict)


if __name__ == '__main__':
    main()
