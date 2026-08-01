"""
Demonstrates a beginner level implementation of 'Closures'
"""

from collections.abc import Callable

from typing import Any, TypedDict


class MemoryVault(TypedDict):
    store: Callable[[str, Any], None]
    recall: Callable[[str], Any]


def mage_counter() -> Callable[[], int]:
    """
    Returns a calls count counter
    """

    count = 0

    def add_one() -> int:
        """
        Adds one to count and returns current value
        """
        nonlocal count
        count += 1
        return count

    return add_one


print("Testing mage counter...")
counter_a = mage_counter()
counter_b = mage_counter()

for _ in range(1, 4):
    print(f"counter_a call {_}: {counter_a()}")

for _ in range(1, 3):
    print(f"counter_b call {_}: {counter_b()}")
print()


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """
    Returns a function that accumulates 'power' over time
    """

    def accumulate_power(power_to_add: int) -> int:
        nonlocal initial_power
        initial_power += power_to_add
        return initial_power

    return accumulate_power


print("Testing spell accumulator...")
accumulator_1 = spell_accumulator(50)
accumulator_2 = spell_accumulator(10)

print("accumulator_1 initial power is 50")
for _ in range(1, 3):
    print(f"accumulator_1 accumulated power is: {accumulator_1(10)}")

print("\naccumulator_2 initial power is 10")
for _ in range(1, 3):
    print(f"accumulator_2 accumulated power is: {accumulator_2(10)}")
print()


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """
    Returns a function that applies specified 'enchantment type'
    """

    return lambda item_name: f"{enchantment_type} {item_name}"


print("Testing enchantment factory...")
factory_1 = enchantment_factory("Flaming")
factory_2 = enchantment_factory("Dark")
item_list = ["Sword", "Staff", "Bow"]

print("'Flaming' factory test:")
for item in item_list:
    print(factory_1(item))
print()
print("'Dark' factory test:")
for item in item_list:
    print(factory_2(item))
print()


def memory_vault() -> MemoryVault:
    """
    Returns a dict with 'store' and 'recall' functions
    """

    storage: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        storage[key] = value

    def recall(key: str) -> Any:
        return storage[key] if key in storage else "Memory not found"

    return {'store': store, 'recall': recall}


print("Testing memory vault...")
mem_vault = memory_vault()
store = mem_vault['store']
recall = mem_vault['recall']
items_dict = {
    "apples": 2,
    "oranges": 3,
    "lemons": 5,
    404: "not found"
}

for key, value in items_dict.items():
    print(f"Storing {value} {key}...")
    store(str(key), value)
print()
for key in items_dict.keys():
    print(f"Recall {str(key)} from vault: {recall(str(key))}")
print("\nTrying to retrieve not valid key ")
print(f"Key is 'bananas': {recall("bananas")}")
