"""
Demonstrates a basic implementation of reduce, partial and wraps tools
from the functools module
"""

import functools

import operator

from collections.abc import Callable

from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    """
    Combines all spell powers
    """

    supported_ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda x, y: x if operator.gt(x, y) else y,
        "min": lambda x, y: x if operator.lt(x, y) else y
    }

    if not spells:
        return 0
    if operation.lower() not in supported_ops.keys():
        print(
            f"Error: operation '{operation}' is not among supported operations"
        )
        print(f"Supported operations: {list(supported_ops.keys())}")
        return 0

    return functools.reduce(supported_ops[operation.lower()], spells)


print("Testing spell reducer...")
spell_powers = [4, 5, 5, 6, 8]
print("Spell powers:", spell_powers)
print(f"Sum: {spell_reducer(spell_powers, 'add')}")
print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
print(f"Max: {spell_reducer(spell_powers, 'max')}")
print(f"Min: {spell_reducer(spell_powers, 'min')}")
print(f"Not supported: {spell_reducer(spell_powers, 'unknown')}")
print(f"Empty list: {spell_reducer([], 'add')}")
print()


def partial_enchanter(
        base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable[[str], str]]:
    """
    Creates three 'specialized' versions of base enchantment
    """

    return {
        "fire": functools.partial(base_enchantment, 50, "fire"),
        "aqua": functools.partial(base_enchantment, 50, "aqua"),
        "wind": functools.partial(base_enchantment, 50, "wind")
    }


def base_enchantment(power: int, element: str, target: str) -> str:
    """
    Basic enchantment for partial enchanter test
    """

    return f"{target.capitalize()} deals {power} {element} damage"


print("Testing partial enchanter...")

partial_enchantments = partial_enchanter(base_enchantment)

for ench in partial_enchantments.values():
    print(ench("Dragon"))
print()


# Maxsize can be None for an unlimited cache size
@functools.lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    """
    Returns the 'nth' Fibonacci number. Final and in between results are
    cached using functools.lru_cache
    """

    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def simple_fibonacci(n: int) -> int:

    if n < 2:
        return n
    return simple_fibonacci(n - 1) + simple_fibonacci(n - 2)


def fib_test() -> None:

    import time

    print("Testing memoized fibonacci...")
    a = time.process_time()
    print(memoized_fibonacci(7))
    b = time.process_time()
    print(f"First memoized call time: {b - a}s")
    print(memoized_fibonacci(7))
    c = time.process_time()
    print(f"Second memoized call time: {c - b}s")
    d = time.process_time()
    print(simple_fibonacci(7))
    e = time.process_time()
    print(f"First not memoized call time: {e - d}s")
    print(simple_fibonacci(7))
    f = time.process_time()
    print(f"Second not memoized call time: {f - e}s")
    print()


fib_test()
print(memoized_fibonacci.cache_info())
print()


def spell_dispatcher() -> Callable[[Any], str]:
    """
    Dispatches an appropiate spell based on arg variable type
    """

    @functools.singledispatch
    def cast(arg: Any) -> str:
        return "Unknown spell type"

    @cast.register
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @cast.register
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @cast.register(list)
    def _(arg: list[Any]) -> str:
        return f"Multi_cast: {len(arg)} spells"

    return cast


dispatcher = spell_dispatcher()
print("Testing spell dispatcher...")
for element in [42, "fireball", [1, 2, 3], {}]:
    print(dispatcher(element))
