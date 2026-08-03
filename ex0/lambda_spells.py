"""
Demonstrates a beginner's level use of lambda functions
"""

from typing import Any


def artifact_sorter(
        artifacts: list[dict[Any, Any]]
) -> list[dict[Any, Any]]:
    """
    Returns same taken list of dicts but sorted by 'power' in desc order
    using a combination of lambda and sorted functions
    """

    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


print("Testing artifact sorter...")
artifacts = [
    {'name': 'Light Prism', 'power': 88, 'type': 'armor'},
    {'name': 'Storm Crown', 'power': 78, 'type': 'focus'},
    {'name': 'Lightning Rod', 'power': 109, 'type': 'relic'},
    {'name': 'Wind Cloak', 'power': 119, 'type': 'focus'}
]
sorted_artifacts = artifact_sorter(artifacts)
print("Unsorted list:")
for _ in artifacts:
    print(
        f"{_['name']} ({_['power']} power)"
    )
print("Sorted list:")
for _ in sorted_artifacts:
    print(
        f"{_['name']} ({_['power']} power)"
    )
print()


def power_filter(
        mages: list[dict[Any, Any]], min_power: int
) -> list[dict[Any, Any]]:
    """
    Returns the 'mages' list filtered by min_power using a combination of
    lambda and filter functions
    """

    return list(filter(lambda x: x['power'] >= min_power, mages))


print("Testing power filter:")
filtered_list = power_filter(artifacts, 80)
print("List filtered with min power = 80")
for _ in filtered_list:
    print(_)
print()


def spell_transformer(spells: list[str]) -> list[str]:
    """
    Returns a list from 'spells' list adding '*' as prefix and suffix to each
    of it's strings using a combination of lambda and map functions
    """

    return list(map(lambda x: '*' + x + '*', spells))


print("Testing spell transformer...")
spells = ['meteor', 'tsunami', 'heal', 'freeze']
transformed_spells = spell_transformer(spells)
for _ in transformed_spells:
    print(_, end="")
print("\n")


def mage_stats(mages: list[dict[Any, Any]]) -> dict[str, int]:
    """
    Returns dict containing max, min and average power found in 'mages' using a
    combination of lambda, max and min functions
    """

    # Using lambdas
    max_v = max(mages, key=lambda x: x["power"])['power']
    min_v = min(mages, key=lambda x: x["power"])['power']
    average_v = sum(list(map(lambda x: x['power'], mages))) / len(mages)

    # Using list comprehensions
    # max_v = max(x['power'] for x in mages)
    # min_v = min(x['power'] for x in mages)
    # average_v = sum(x['power'] for x in mages) / len(mages)

    return {'max': max_v, 'min': min_v, 'average': average_v}


print("Testing mage stats...")
mages = [
    {'name': 'Sage', 'power': 58, 'element': 'earth'},
    {'name': 'Ash', 'power': 72, 'element': 'wind'},
    {'name': 'Casey', 'power': 90, 'element': 'wind'},
    {'name': 'Morgan', 'power': 80, 'element': 'shadow'},
    {'name': 'Alex', 'power': 80, 'element': 'earth'}
]
stats = mage_stats(mages)
print("All mages:")
for _ in mages:
    print(_)
print(stats)
