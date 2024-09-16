import datetime
from typing import Any, List, Dict

# Good Comments Examples

# 1. Legal Comments
# The above copyright notice is an example of a legal comment.


# 2. Informative Comments
def get_user_status(user_id: int) -> str:
    # Returns 'active', 'inactive', or 'suspended'
    # based on the user's current status in the database
    return "active"


# 3. Explanation of Intent
def sort_users(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    # We're using a stable sort here to maintain the relative order
    # of users with the same last name
    return sorted(users, key=lambda u: u["last_name"])


# 4. Clarification
def complex_calculation(x: float, y: float) -> float:
    # The magic number 0.3 is the result of a complex business logic
    # that determines the optimal threshold for our use case
    return x * y * 0.3


# 5. Warning of Consequences
def delete_user(user_id: int) -> None:
    # WARNING: This operation cannot be undone. Ensure you have a backup.
    pass


# 6. TODO Comments
def process_data(data: List[int]) -> List[int]:
    # TODO: Optimize this function for large datasets
    return [item * 2 for item in data]


# Examples of Bad Comments (and how to avoid them)


# 1. Redundant Comments (Avoid)
def add(a: int, b: int) -> int:
    # This function adds two numbers
    return a + b


# Better: Let the function name speak for itself
def add(a: int, b: int) -> int: # type: ignore
    return a + b


# 2. Misleading Comments (Avoid)
def get_users() -> List[Dict[str, Any]]:
    all_users = get_all_users()  # type: ignore
    # Returns active users
    return [user for user in all_users if user["status"] in ("active", "suspended")]


# Better: Make the comment accurate or, preferably, make the code self-explanatory
def get_active_and_suspended_users() -> List[Dict[str, Any]]:
    all_users = get_all_users()  # type: ignore
    return [user for user in all_users if user["status"] in ("active", "suspended")]


# 3. Mandated Comments (Avoid)
class User:
    """
    This class represents a user.
    """

    def __init__(self, name: str):
        """
        Initializes a new User instance.
        :param name: The name of the user.
        """
        self.name = name


# Better: Only add comments when they provide additional context
class User:  # type: ignore
    def __init__(self, name: str):
        self.name = name


# 4. Journal Comments (Avoid)
# 2024-03-15: Added email field
# 2024-03-20: Added phone field
class Contact:
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone


# Better: Use version control systems to track changes


# 5. Noise Comments (Avoid)
def get_current_date() -> datetime.date:
    # This function returns the current date
    return datetime.date.today()


# Better: Let the function name speak for itself
def get_current_date() -> datetime.date:  # type: ignore
    return datetime.date.today()


# Example of explaining yourself in code
# Instead of:
# if (employee.flags & HOURLY_FLAG) and (employee.age > 65)
# Better:
class Employee:
    def __init__(self, hourly: bool, age: int):
        self.hourly = hourly
        self.age = age


def is_eligible_for_full_benefits(employee: Employee) -> bool:
    return employee.is_hourly_employee() and employee.is_senior_citizen()  # type: ignore


# Remember: The best comment is the one you found a way not to write!
