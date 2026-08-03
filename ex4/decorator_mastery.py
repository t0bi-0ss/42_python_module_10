"""
Demonstrates a beginner's level implementation of
custom decorators
"""

import functools

from collections.abc import Callable

import time

from typing import Any

import inspect


def spell_timer(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """
    Decorator to calculate wrapped function's time of execution
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        b = time.process_time()
        res = func(*args, **kwargs)
        a = time.process_time()
        print(f"Casting {func.__name__}...")
        print(f"Spell completed in {a - b:.4f} seconds")
        return res
    return wrapper


@spell_timer
def simple_fireball(w: str = "") -> str:
    return f"Fireball cast!{w}"


print("Testing spell timer...")
res = simple_fireball("")
print(f"Result: {res}\n")


def power_validator(min_power: int) -> Callable[[Any], Any]:
    """
    Decorator that validates min power before wrapped functions execution
    """

    def func_taker(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if 'power' in kwargs and isinstance(kwargs['power'], int):
                return func(*args, **kwargs) if kwargs['power'] >= min_power \
                    else "Insufficient power for this spell"
            else:
                pow_index = -1
                params = enumerate(inspect.signature(func).parameters.values())
                for i, param in params:
                    if param.name == 'power':
                        pow_index = i
                if pow_index >= 0 and isinstance(args[pow_index], int):
                    return func(*args, **kwargs) \
                        if args[pow_index] >= min_power \
                        else "Insufficient power for this spell"
                else:
                    return "No ('power': int) parameter could be found"
        return wrapper
    return func_taker


@power_validator(5)
def powered_fireball(power: int) -> str:
    return f"Fireball of power: {power}"


@power_validator(5)
def wrong_implementation(power: str) -> str:
    return f"Something {power}"


print("Testing power validator...")
print("Test with sufficient power:")
print(powered_fireball(power=5))
print("Test with insufficient power")
print(powered_fireball(4))
print("Test with an invalid function being wrapped")
print(wrong_implementation("s"))
print()


def retry_spell(max_attempts: int) -> Callable[[Any], Any]:
    """
    Decorator that retries failed spells up to a max number of attempts
    """

    failed_attempts = 0

    def func_taker(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            nonlocal failed_attempts
            if failed_attempts < max_attempts:
                try:
                    res = func(*args, **kwargs)
                except (ValueError, TypeError):
                    failed_attempts += 1
                    if failed_attempts <= max_attempts - 1:
                        print(
                            "Spell failed, retrying...",
                            f"(attempt {failed_attempts}/{max_attempts})"
                        )
                    else:
                        print(
                            "Spell casting failed"
                            f" after {max_attempts} attempts"
                        )
                else:
                    return res
        return wrapper
    return func_taker


@retry_spell(3)
def simple_func(word: str) -> str:
    return word + "abc"


print("Testing retry spell...")
words = [1, 2, "a", 4]
for w in words:
    res = simple_func(w)
    if res:
        print(res)
print()


class MageGuild():

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        for w in name.split():
            if not w.isalpha() or len(w) < 3:
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


print("Testing MageGuild...")
print("\nTesting validate_mage_name...")
print(f"Sam: {MageGuild.validate_mage_name('Sam')}")
print(f"NO: {MageGuild.validate_mage_name('NO')}")
print(f"Sam%: {MageGuild.validate_mage_name('Sam%')}")
print(f"Ron Whisky: {MageGuild.validate_mage_name('Ron Whisky')}")
print(f"Ron W!: {MageGuild.validate_mage_name('Ron W!')}")

print(
    "\nInstatiate a 'MageGuild' object",
    "in order to be able to use 'cast_spell':"
)
mage = MageGuild()
print(mage.cast_spell("Lightning", 15))
print(mage.cast_spell("Lightning", 9))
