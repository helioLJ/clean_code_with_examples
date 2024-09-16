# Clean Code - Chapter 5: Formatting Examples

# Vertical Formatting

# File Size
# This file should be kept relatively small (200-500 lines)

# Newspaper Metaphor
from typing import Any


def high_level_function() -> None:
    """This function represents a high-level concept."""
    # Implementation details...
    pass


def low_level_function() -> None:
    """This function represents a low-level implementation detail."""
    # Specific implementation...
    pass


# Vertical Openness
def function_1() -> None:
    # Implementation...
    pass


# Blank line to separate functions
def function_2() -> None:
    # Implementation...
    pass


# Vertical Density
class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def get_info(self) -> str:
        return f"{self.name}, {self.age} years old"


# Vertical Distance
class Calculator:
    def add(self, a: int, b: int) -> int:
        return a + b

    def subtract(self, a: int, b: int) -> int:
        return a - b

    # Other related methods...


# Horizontal Formatting

# Line Length
long_string = (
    "This is an example of a long string that we might want to "
    "break into multiple lines to avoid exceeding the recommended "
    "line length of 80-120 characters."
)


# Horizontal Openness and Density
def calculate(x: int, y: int, z: int) -> int:
    return (x + y) * z


# Indentation
def complex_function(condition_1: bool, condition_2: bool, items: list[Any]) -> int:
    if condition_1:
        if condition_2:
            for item in items:
                if item.is_valid():
                    item.process()
                else:
                    item.skip()
        else:
            handle_else_case()  # type: ignore
    return 0


# Team Rules
# This entire file should follow the team's agreed-upon formatting rules


# Uncle Bob's Formatting Rules
def example_function(arg1: int, arg2: int) -> int:
    result = do_something(arg1, arg2)  # type: ignore
    if result > 100:
        handle_large_result(result)  # type: ignore
    else:
        handle_small_result(result)  # type: ignore
    return 0
