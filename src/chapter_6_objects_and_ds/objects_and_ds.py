# Data Abstraction
class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def distance_from_origin(self) -> float:
        return float((self._x**2 + self._y**2) ** 0.5)


# Objects vs. Data Structures
class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def area(self) -> int:
        return self._width * self._height


class RectangleData:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height


def calculate_area(rectangle_data: RectangleData) -> int:
    return rectangle_data.width * rectangle_data.height


# Law of Demeter
class Wallet:
    def __init__(self, money: int):
        self._money = money

    def get_money(self, amount: int) -> int:
        if amount <= self._money:
            self._money -= amount
            return amount
        return 0


class Person:
    def __init__(self, name: str, wallet: Wallet):
        self._name = name
        self._wallet = wallet

    def buy_item(self, cost: int) -> int:
        return self._wallet.get_money(cost)


# Data Transfer Objects (DTOs)
class UserDTO:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


# Active Record
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def save(self) -> None:
        # Save user to database
        pass

    @classmethod
    def find(cls, user_id: int) -> "User":
        # Find user in database
        return cls(name="John Doe", email="john.doe@example.com")


# Separation of Concerns
class UserData:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


class UserService:
    @staticmethod
    def validate_email(email: str) -> bool:
        # Validate email
        return True

    @staticmethod
    def create_user(user_data: UserData) -> None:
        if UserService.validate_email(user_data.email):
            # Create user in database
            pass
