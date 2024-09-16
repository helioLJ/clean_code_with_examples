from datetime import datetime
from typing import Any


class Account:
    def __init__(self, balance: float):
        self.balance = balance


# Small Functions
def calculate_area_of_circle(radius: float) -> float:
    return 3.14 * radius**2


# Do One Thing
def send_email(to_address: str, subject: str, body: str) -> None:
    # This function should only handle sending an email
    # Not composing the email or validating addresses
    pass


# One Level of Abstraction per Function
def make_breakfast() -> None:
    prepare_eggs()
    toast_bread()  # type: ignore
    brew_coffee()  # type: ignore


def prepare_eggs() -> None:
    # Lower level details of egg preparation
    pass


# Switch Statements (using polymorphism instead)
class Shape:
    def area(self) -> float:
        raise NotImplementedError("Subclass must implement abstract method")


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius**2


class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side**2


# Use Descriptive Names
def find_active_accounts_older_than(days: int) -> list[Account]:
    # Implementation
    return []


# Function Arguments
def connect() -> None:  # No arguments
    pass


def square(number: float) -> float:  # One argument
    return number**2


def power(base: float, exponent: float) -> float:  # Two arguments
    return float(base**exponent)


# Common Monadic Forms
def is_prime(number: int) -> bool:  # Asks a question
    # Implementation
    return True


def print_message(message: str) -> None:  # Performs an operation
    print(message)


# Argument Objects
class DateRange:
    def __init__(self, start_date: datetime, end_date: datetime):
        self.start_date = start_date
        self.end_date = end_date


def get_sales_report(date_range: DateRange) -> None:
    # Implementation using date_range.start_date and date_range.end_date
    pass


# Verbs and Keywords
def delete_page(page_id: int) -> None:
    # Implementation
    pass


def assert_equals_and_not_null(expected: Any, actual: Any) -> None:
    # Implementation
    pass


# Have No Side Effects
def calculate_total_price(items: list[Any]) -> float:
    return float(sum(float(item.price) for item in items))
    # This function doesn't modify any external state


# Command Query Separation
def set_attribute(attribute: Any, value: Any) -> None:
    # Sets an attribute but doesn't return anything
    pass


def get_attribute(attribute: Any) -> Any:
    # Returns the value of an attribute but doesn't modify anything
    pass


# Prefer Exceptions to Returning Error Codes
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Extract Try/Catch Blocks
def delete_page_and_handle_errors(page_id: int) -> None:
    try:
        page = database.get_page(page_id)  # type: ignore
        database.delete(page)  # type: ignore
    except DatabaseError as e:  # type: ignore
        log_error(f"Failed to delete page {page_id}: {str(e)}")  # type: ignore
        raise


# Don't Repeat Yourself (DRY)
def validate_user_input(input_string: str) -> None:
    if not input_string:
        raise ValueError("Input cannot be empty")
    if len(input_string) < 3:
        raise ValueError("Input must be at least 3 characters long")
    # More validation logic...


# Example usage of the validation function
def process_username(username: str) -> None:
    validate_user_input(username)
    # Process the username...


def process_email(email: str) -> None:
    validate_user_input(email)
    # Process the email...


# Structured Programming (with an example of when multiple returns can be clear)
def get_parity(n: int) -> str:
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
