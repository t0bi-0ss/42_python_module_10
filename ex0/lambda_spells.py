"""
Demonstrates a beginner's level use of lambda functions
"""

from typing import Any


def artifact_sorter(
        artifacts: list[dict[Any, Any]]
) -> list[dict[Any, Any]]:
    """
    Returns same taken list of dicts but sorted using a combination of lambda
    and sorted functions
    """

    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(
        mages: list[dict[Any, Any]], min_power: int
) -> list[dict[Any, Any]]:
    """
    Returns the 'mages' list filtered by min_power using a combination of
    lambda and filter functions
    """

    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """
    Returns a list from 'spells' list adding '*' as prefix and suffix to each
    of it's strings using a combination of lambda and map functions
    """

    return list(map(lambda x: '*' + x + '*', spells))


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
