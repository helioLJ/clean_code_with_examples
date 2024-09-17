# Helper classes
class Order:
    def __init__(self, order_dict: dict[str, Any]) -> None:
        self.customer_id = order_dict["customer_id"]
        self.items = order_dict["items"]
        self.total = order_dict["total"]


class PaymentGateway:
    def process_payment(self, amount: float) -> bool:
        # Simulating payment processing
        return True


class OrderRepository:
    def save(self, order: Order) -> bool:
        # Simulating order saving
        return True


class UserRepository:
    def find_by_id(self, user_id: str) -> str:
        # Simulating database query
        return f"User with id {user_id}"


class AdminUser:
    def __init__(self) -> None:
        self.permissions: list[str] = ["read", "write", "delete"]


class RegularUser:
    def __init__(self) -> None:
        self.permissions: list[str] = ["read"]


# Clean Code - Chapter 11: Systems

# 1. Separate Construction from Use
from typing import Any, Callable


class DatabaseConnection:
    def __init__(self, host: str, port: int, username: str, password: str) -> None:
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def connect(self) -> None:
        print(f"Connecting to database at {self.host}:{self.port}")


# 2. Separation of Main
def main() -> None:
    db = DatabaseConnection("localhost", 5432, "user", "password")
    app = Application(db)
    app.run()


class Application:
    def __init__(self, db_connection: DatabaseConnection) -> None:
        self.db = db_connection

    def run(self) -> None:
        self.db.connect()
        print("Application is running")


# 3. Factories
class UserFactory:
    @staticmethod
    def create(user_type: str) -> AdminUser | RegularUser:
        if user_type == "admin":
            return AdminUser()
        elif user_type == "regular":
            return RegularUser()
        else:
            raise ValueError("Invalid user type")


# 4. Dependency Injection
class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def get_user(self, user_id: str) -> str:
        return self.user_repository.find_by_id(user_id)


# 5. Aspect-Oriented Programming (simplified example)
def logging_aspect(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Logging: Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Logging: {func.__name__} completed")
        return result

    return wrapper


@logging_aspect
def business_logic() -> None:
    print("Executing business logic")


# 6. Test-Driven System Architecture
class OrderService:
    def __init__(
        self, order_repository: OrderRepository, payment_gateway: PaymentGateway
    ) -> None:
        self.order_repository = order_repository
        self.payment_gateway = payment_gateway

    def place_order(self, order: Order) -> bool:
        if self.payment_gateway.process_payment(order.total):
            return self.order_repository.save(order)
        return False


# 7. Domain-Specific Language (DSL) example
class OrderDSL:
    def __init__(self) -> None:
        self.order: dict[str, Any] = {}

    def for_customer(self, customer_id: int) -> "OrderDSL":
        self.order["customer_id"] = customer_id
        return self

    def with_item(self, item_id: str, quantity: int) -> "OrderDSL":
        if "items" not in self.order:
            self.order["items"] = []
        self.order["items"].append({"item_id": item_id, "quantity": quantity})
        return self

    def build(self) -> Order:
        return Order(self.order)


if __name__ == "__main__":
    main()

    # Using the DSL
    order = OrderDSL().for_customer(123).with_item("A1", 2).with_item("B2", 1).build()
    print(
        f"Order created for customer {order.customer_id} with {len(order.items)} items"
    )

    # Demonstrating AOP
    business_logic()
