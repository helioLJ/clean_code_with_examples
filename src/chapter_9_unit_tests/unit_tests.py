import unittest
from datetime import datetime


# Example class to be tested
class User:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        self.last_login: datetime | None = None

    def login(self) -> None:
        self.last_login = datetime.now()


# Example of the Three Laws of TDD
class TestUserLogin(unittest.TestCase):
    def test_user_login_updates_last_login(self) -> None:
        # First Law: Write a failing test
        user = User("John Doe", "john@example.com")
        user.login()
        self.assertIsNotNone(user.last_login)


# Example of Clean Tests
class TestUserCreation(unittest.TestCase):
    def test_user_creation(self) -> None:
        name = "Jane Doe"
        email = "jane@example.com"
        user = User(name, email)
        self.assertEqual(user.name, name)
        self.assertEqual(user.email, email)


# Example of Domain-Specific Testing Language
class UserTestCase(unittest.TestCase):
    def create_user(self, name: str, email: str) -> User:
        return User(name, email)

    def assert_user_properties(self, user: User, name: str, email: str) -> None:
        self.assertEqual(user.name, name)
        self.assertEqual(user.email, email)

    def test_user_creation_with_dsl(self) -> None:
        user = self.create_user("Alice", "alice@example.com")
        self.assert_user_properties(user, "Alice", "alice@example.com")


# Example of Single Concept per Test
class TestUserProperties(unittest.TestCase):
    def test_user_name(self) -> None:
        user = User("Bob", "bob@example.com")
        self.assertEqual(user.name, "Bob")

    def test_user_email(self) -> None:
        user = User("Bob", "bob@example.com")
        self.assertEqual(user.email, "bob@example.com")


# Example of F.I.R.S.T. Principles
class TestUserFIRST(unittest.TestCase):
    def test_user_login_fast(self) -> None:
        user = User("Charlie", "charlie@example.com")
        user.login()
        self.assertIsNotNone(user.last_login)

    def test_user_creation_independent(self) -> None:
        user1 = User("David", "david@example.com")
        user2 = User("Eve", "eve@example.com")
        self.assertNotEqual(user1, user2)

    def test_user_email_repeatable(self) -> None:
        user = User("Frank", "frank@example.com")
        self.assertEqual(user.email, "frank@example.com")

    def test_user_name_self_validating(self) -> None:
        user = User("Grace", "grace@example.com")
        self.assertEqual(user.name, "Grace")


if __name__ == "__main__":
    unittest.main()
