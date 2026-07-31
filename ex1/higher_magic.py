"""
Demonstrates a beginner level use and implementation of higher order functions
"""

from collections.abc import Callable


# Basic functions to be use in this project
def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fire_ball(target: str, power: int) -> str:
    return f"Fire Ball hits {target} for {power} damage"


def some_condition(target: str, power: int) -> bool:
    if target and power >= 5:
        return True
    elif target:
        print("Spell was not strong enough (<5)")
        return False
    else:
        print("No target specified")
        return False


# Higher order functions

def spell_combiner(
        spell_1: Callable[[str, int], str],
        spell_2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    """
    Returns a 'Callable' that combines both passed spells
    """

    if not callable(spell_1) or not callable(spell_2):
        raise ValueError("One or both spells is/are not 'Callable'")

    return lambda target, power: (
        spell_1(target, power), spell_2(target, power)
    )


# Test spell_combiner
print("Testing spell combiner...")
combined = spell_combiner(fire_ball, heal)
print(", ".join(combined("Dragon", 5)))
print()


def power_amplifier(
        base_spell: Callable[[str, int], str], multiplier: int
) -> Callable[[str, int], str]:
    """
    Returns a 'Callable' 'amplified' version of base_spell
    """

    if not callable(base_spell):
        raise ValueError("Spell is not 'Callable'")

    return lambda target, power: base_spell(target, power * multiplier)


# Power amplifier test
print("Testing power amplifier...")
amplified = power_amplifier(fire_ball, 5)
print("Power is 5 but multiplier is 5 so...")
print(amplified("Dragon", 5))
print()


def conditional_caster(
        condition: Callable[[str, int], bool], spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    """
    Returns a new spell that only casts if a condition is met
    """

    if not callable(condition) or not callable(spell):
        raise ValueError("Condition or spell is/are not 'Callable'")

    return lambda target, power: spell(target, power) \
        if condition(target, power) else "Spell fizzled..."


# Conditional caster test
print("Testing conditional caster...")
conditioned = conditional_caster(some_condition, fire_ball)
print(conditioned("Dragon", 4))
print(conditioned("Dragon", 5))
print()


def spell_sequence(
        spells: list[Callable[[str, int], str]]
) -> Callable[[str, int], list[str]]:
    """
    Returns a 'Callable' that casts all spells in order
    """

    if [_ for _ in spells if not callable(_)]:
        raise ValueError("One or more spell/s is/are not 'Callable'")

    def cast_spells(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return cast_spells


# Spell sequence test
print("Testing spell sequence caster...")
sequence = spell_sequence([fire_ball, heal])
print(sequence("Dragon", 5))
