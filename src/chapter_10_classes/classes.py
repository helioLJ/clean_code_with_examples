# Class Organization
class WellOrganizedClass:
    PUBLIC_STATIC_CONSTANT = 42

    _private_static_variable = "I'm static"

    def __init__(self) -> None:
        self._private_instance_variable: str = "I'm an instance variable"

    def public_method(self) -> str:
        return self._private_utility_method()

    def _private_utility_method(self) -> str:
        return "I support the public method"


# Encapsulation
class EncapsulatedClass:
    def __init__(self) -> None:
        self.__private_variable: str = "I'm private"

    def __private_method(self) -> str:
        return "I'm a private method"

    def public_method(self) -> str:
        return self.__private_method()


# Single Responsibility Principle (SRP)
class VersionManager:
    def __init__(self) -> None:
        self.version: str = "1.0"

    def get_version(self) -> str:
        return self.version


class GUIManager:
    def __init__(self) -> None:
        self.elements: list[str] = []

    def add_element(self, element: str) -> None:
        self.elements.append(element)


# Cohesion
class CohesiveClass:
    def __init__(self) -> None:
        self.data: list[str] = []

    def add_item(self, item: str) -> None:
        self.data.append(item)

    def remove_item(self, item: str) -> None:
        self.data.remove(item)

    def get_items(self) -> list[str]:
        return self.data


# Organizing for Change (Open-Closed Principle)
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius**2


# Isolating from Change (Dependency Inversion Principle)
class DatabaseInterface(ABC):
    @abstractmethod
    def save(self, data: str) -> None:
        pass


class SQLDatabase(DatabaseInterface):
    def save(self, data: str) -> None:
        print(f"Saving {data} to SQL database")


class NoSQLDatabase(DatabaseInterface):
    def save(self, data: str) -> None:
        print(f"Saving {data} to NoSQL database")


class DataManager:
    def __init__(self, database: DatabaseInterface):
        self.database = database

    def save_data(self, data: str) -> None:
        self.database.save(data)


# Example Refactoring: Prime Number Generator
class PrimeGenerator:
    def __init__(self, max_value: int) -> None:
        self.max_value = max_value
        self.primes: list[int] = []

    def generate_primes(self) -> list[int]:
        self._initialize_array()
        self._cross_out_multiples()
        self._collect_primes()
        return self.primes

    def _initialize_array(self) -> None:
        self.is_prime: list[bool] = [True] * (self.max_value + 1)
        self.is_prime[0] = self.is_prime[1] = False

    def _cross_out_multiples(self) -> None:
        for i in range(2, int(self.max_value**0.5) + 1):
            if self.is_prime[i]:
                for j in range(i * i, self.max_value + 1, i):
                    self.is_prime[j] = False

    def _collect_primes(self) -> None:
        self.primes = [i for i in range(2, self.max_value + 1) if self.is_prime[i]]


# Usage example
if __name__ == "__main__":
    prime_gen = PrimeGenerator(30)
    primes = prime_gen.generate_primes()
    print(f"Primes up to 30: {primes}")


# Liskov Substitution Principle (LSP)
class Bird:
    def fly(self) -> str:
        return "I'm flying!"


class Sparrow(Bird):
    pass  # Sparrow can use the parent's fly method


class Ostrich(Bird):
    def fly(self) -> str:
        return "I can't fly, but I can run fast!"


def make_bird_fly(bird: Bird) -> str:
    return bird.fly()


# Usage
sparrow = Sparrow()
ostrich = Ostrich()
print(make_bird_fly(sparrow))  # Output: I'm flying!
print(make_bird_fly(ostrich))  # Output: I can't fly, but I can run fast!

# Interface Segregation Principle (ISP)
from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print_document(self, document: str) -> None:
        pass


class Scanner(ABC):
    @abstractmethod
    def scan_document(self) -> str:
        pass


class Fax(ABC):
    @abstractmethod
    def fax_document(self, document: str) -> None:
        pass


class SimplePrinter(Printer):
    def print_document(self, document: str) -> None:
        print(f"Printing: {document}")


class AllInOnePrinter(Printer, Scanner, Fax):
    def print_document(self, document: str) -> None:
        print(f"Printing: {document}")

    def scan_document(self) -> str:
        return "Scanned document content"

    def fax_document(self, document: str) -> None:
        print(f"Faxing: {document}")


# Usage
simple_printer = SimplePrinter()
all_in_one = AllInOnePrinter()

simple_printer.print_document("Hello, World!")
all_in_one.print_document("Hello, World!")
print(all_in_one.scan_document())
all_in_one.fax_document("Hello, World!")
