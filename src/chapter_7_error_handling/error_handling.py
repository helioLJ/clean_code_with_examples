# Clean Code - Chapter 7: Error Handling Examples

from typing import Any


class InsufficientFundsError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(f"Insufficient funds: {message}")


# 1. Use Exceptions Rather Than Return Codes
class Account:
    def __init__(self, balance: float):
        self.balance = balance


def withdraw(account: Account, amount: float) -> None:
    if account.balance >= amount:
        account.balance -= amount
    else:
        raise InsufficientFundsError(f"Balance: {account.balance}, Requested: {amount}")


# 2. Write Your Try-Catch-Finally Statement First
def transfer_money(from_account: Account, to_account: Account, amount: float) -> None:
    try:
        withdraw(from_account, amount)
        to_account.deposit(amount)  # type: ignore
    except InsufficientFundsError as e:
        log_error(f"Transfer failed: {str(e)}")  # type: ignore
        raise
    finally:
        notify_transfer_attempt(from_account, to_account, amount)  # type: ignore


# 3. Use Unchecked Exceptions (Python doesn't have checked exceptions, so this is the default)


# 4. Provide Context with Exceptions
class APICallError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(f"API call failed: {message}")


# 5. Define Exception Classes in Terms of a Caller's Needs
class ThirdPartyAPIError(Exception):
    pass


def call_external_api() -> Any:
    try:
        # Call to third-party API
        response = third_party_api.make_request()  # type: ignore
        return response
    except ThirdPartyAPIError as e:
        raise APICallError(f"Error calling external API: {str(e)}")


# 6. Define the Normal Flow
class Employee:
    def get_pay(self) -> Any:
        raise NotImplementedError("Subclass must implement abstract method")


class RegularEmployee(Employee):
    def __init__(self, base_salary: float):
        self.base_salary = base_salary

    def get_pay(self) -> float:
        return self.base_salary


class CommissionedEmployee(Employee):
    def __init__(self, base_salary: float, commission: float):
        self.base_salary = base_salary
        self.commission = commission

    def get_pay(self) -> float:
        return self.base_salary + self.commission


class PayrollSystem:
    def calculate_pay(self, employee: Employee) -> Any:
        return employee.get_pay()


class EmployeeNotFoundError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(f"Employee not found: {message}")


# 7. Don't Return Null
def get_employee(employee_id: int) -> Employee | Any:
    employee = database.find_employee(employee_id)  # type: ignore
    if employee is None:
        raise EmployeeNotFoundError(f"No employee found with id: {employee_id}")
    return employee


# 8. Don't Pass Null
def process_employee(employee: Employee | Any) -> None:
    if employee is None:
        raise ValueError("Employee cannot be None")
    # Process employee...


# Usage example
def main() -> None:
    try:
        employee = get_employee(123)
        process_employee(employee)
    except EmployeeNotFoundError as e:
        print(f"Error: {str(e)}")
    except ValueError as e:
        print(f"Invalid input: {str(e)}")


if __name__ == "__main__":
    main()
