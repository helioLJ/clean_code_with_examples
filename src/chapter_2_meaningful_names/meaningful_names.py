class User:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self.is_active = is_active


class Account:
    def __init__(self, balance: float):
        self.balance = balance


# Use Intention-Revealing Names
def get_active_users(users: list[User]) -> list[User]:
    return [user for user in users if user.is_active]


# Avoid Disinformation
# Bad: list_of_accounts = {'john': 1000, 'jane': 2000}  # This is actually a dictionary
# Good:
account_balances = {"john": 1000, "jane": 2000}


# Make Meaningful Distinctions
# Bad: def process_data(a1, a2, a3): ...
# Good:
def process_user_data(name: str, age: int, email: str) -> None:
    # Process user data here
    pass


# Use Pronounceable Names
# Bad: genymdhms = ...
# Good:
generation_timestamp = ...

# Use Searchable Names
# Bad: s = 3600
# Good:
SECONDS_PER_HOUR = 3600


# Avoid Encodings
# Bad: class IShapeFactory: ...
# Good:
class ShapeFactory:
    # Shape factory implementation
    pass


# Class and Method Names
class UserAccount:
    def calculate_balance(self) -> float:
        # Calculate balance logic
        return 0.0


# Don't Be Cute
# Bad: def whack(): ...
# Good:
def kill_process() -> None:
    # Kill process logic
    pass


# Pick One Word per Concept
# Consistent use of 'get' for retrieval operations
def get_user(user_id: int) -> User:
    # Retrieve user logic
    return User(name="John", age=30, is_active=True)


def get_account(account_id: int) -> Account:
    # Retrieve account logic
    return Account(balance=1000.0)


# Use Solution Domain Names
class BinaryTree:
    # Binary tree implementation
    pass


# Use Problem Domain Names
class InvoiceCalculator:
    def calculate_total_with_tax(
        self, items: list[dict[str, float]], tax_rate: float
    ) -> float:
        # Calculate invoice total with tax
        return 0.0


# Add Meaningful Context
class Address:
    def __init__(self, street: str, city: str, state: str, zip_code: str):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code


# Don't Add Gratuitous Context
# Bad: class CustomerObject: ...
# Good:
class Customer:
    # Customer implementation
    pass
