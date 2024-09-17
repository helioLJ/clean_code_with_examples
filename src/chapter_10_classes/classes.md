# Clean Code - Chapter 10 Summary: Classes

## Class Organization
- **Variable Declaration Order**: Start with public static constants, followed by private static variables, and then private instance variables. Avoid public variables.
- **Function Order**: Public functions should follow variables, with private utilities placed immediately after the public functions they support, following the stepdown rule for readability.

## Encapsulation
- **Privacy Preference**: Keep variables and utility functions private unless necessary for testing, in which case protected or package scope may be used. Loosening encapsulation is a last resort.

## Classes Should Be Small
- **Size Principle**: Classes should be small, measured by responsibilities rather than lines of code. A class should have a single responsibility, aligning with the Single Responsibility Principle (SRP).

## Single Responsibility Principle (SRP)
- **Definition**: A class should have one reason to change, meaning it should encapsulate a single responsibility.
- **Example**: The `SuperDashboard` class is too large because it handles multiple responsibilities, such as version tracking and GUI management.

## Cohesion
- **Cohesion in Classes**: Classes should have a small number of instance variables, with methods that manipulate these variables. High cohesion means methods and variables are interdependent and logically connected.

## Maintaining Cohesion
- **Splitting Classes**: When functions share variables, consider splitting them into separate classes to maintain high cohesion and create smaller, more focused classes.

## Organizing for Change
- **Reducing Change Risk**: Organize classes to minimize the risk of change. Use the Open-Closed Principle (OCP) to allow classes to be open for extension but closed for modification.

## Isolating from Change
- **Dependency Management**: Use interfaces and abstract classes to isolate dependencies and reduce the impact of changes. This adheres to the Dependency Inversion Principle (DIP), which suggests depending on abstractions rather than concrete details.

## Example Refactoring
- **Prime Number Program**: Refactor a monolithic function into smaller classes and functions, each with a clear responsibility, improving readability and maintainability.
