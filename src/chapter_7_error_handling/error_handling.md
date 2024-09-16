# Clean Code - Chapter 7 Summary: Error Handling

## Introduction
Error handling is a crucial aspect of programming, ensuring that code can handle unexpected situations gracefully. However, excessive error handling can obscure the main logic of the code, making it difficult to understand. This chapter outlines techniques to write clean and robust code that handles errors effectively.

## Use Exceptions Rather Than Return Codes
- **Old Approach**: Previously, error handling involved setting error flags or returning error codes, which cluttered the caller's logic.
- **Modern Approach**: Use exceptions to handle errors, as they separate error handling from the main logic, making the code cleaner and easier to understand.

## Write Your Try-Catch-Finally Statement First
- **Scope Definition**: Exceptions define a scope within your program. The try block is like a transaction, and the catch block must leave the program in a consistent state.
- **Best Practice**: Start with a try-catch-finally statement to define what the user should expect, regardless of errors.

## Use Unchecked Exceptions
- **Debate on Checked Exceptions**: Checked exceptions can violate the Open/Closed Principle by requiring changes in method signatures up the call hierarchy.
- **Recommendation**: Use unchecked exceptions to avoid cascading changes and maintain encapsulation.

## Provide Context with Exceptions
- **Informative Messages**: Each exception should provide enough context to determine the source and nature of the error. Include informative error messages with exceptions.

## Define Exception Classes in Terms of a Caller’s Needs
- **Error Classification**: Define exception classes based on how they are caught, rather than their source or type.
- **Example**: Wrap third-party APIs to simplify exception handling and reduce dependencies.

## Define the Normal Flow
- **Separation of Concerns**: Separate business logic from error handling to maintain a clean algorithm.
- **Special Case Pattern**: Use special case objects to handle exceptional behavior, simplifying client code.

## Don’t Return Null
- **Avoid Null Returns**: Returning null invites errors and requires excessive null checks.
- **Alternative**: Throw exceptions or return special case objects instead of null.

## Don’t Pass Null
- **Avoid Passing Null**: Passing null into methods can lead to runtime errors. Instead, forbid passing null by default to reduce careless mistakes.

## Conclusion
Clean code should be both readable and robust. By treating error handling as a separate concern, we can write maintainable and understandable code.