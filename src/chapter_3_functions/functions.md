# Clean Code - Chapter 3 Summary: Functions

## Introduction
- Functions are the primary unit of organization in programming.
- Writing clear and effective functions is crucial for maintainable code.

## Small Functions
- Functions should be small, ideally just a few lines long.
- Smaller functions are easier to read, understand, and maintain.

## Do One Thing
- Functions should do one thing and do it well.
- A function should only perform tasks that are one level of abstraction below its name.

## One Level of Abstraction per Function
- Keep all statements in a function at the same level of abstraction.
- This helps maintain clarity and focus within the function.

## Reading Code from Top to Bottom: The Stepdown Rule
- Code should read like a top-down narrative, with each function followed by those at the next level of abstraction.

## Switch Statements
- Switch statements should be minimized and encapsulated in low-level classes.
- Use polymorphism to handle variations instead of switch statements.

## Use Descriptive Names
- Choose names that clearly describe the function's purpose.
- Descriptive names improve readability and help set expectations.

## Function Arguments
- The ideal number of arguments is zero, followed by one or two.
- Avoid functions with more than three arguments unless absolutely necessary.

## Common Monadic Forms
- Functions with one argument should either ask a question or perform an operation on the argument.

## Flag Arguments
- Avoid using boolean flag arguments, as they indicate a function is doing more than one thing.

## Dyadic and Triadic Functions
- Functions with two or three arguments are harder to understand and should be used sparingly.

## Argument Objects
- When a function requires multiple arguments, consider encapsulating them in an object.

## Verbs and Keywords
- Use verbs and keywords in function names to clarify their purpose and the role of arguments.

## Have No Side Effects
- Functions should not have hidden side effects that alter the state of the system unexpectedly.

## Command Query Separation
- Functions should either perform an action or return information, but not both.

## Prefer Exceptions to Returning Error Codes
- Use exceptions for error handling to separate error processing from normal logic.

## Extract Try/Catch Blocks
- Extract try/catch blocks into separate functions to keep error handling distinct from normal processing.

## Error Handling Is One Thing
- Functions should focus on either normal processing or error handling, not both.

## Don’t Repeat Yourself
- Avoid code duplication to reduce maintenance effort and potential errors.

## Structured Programming
- While structured programming principles are useful, small functions can sometimes benefit from multiple return statements for clarity.

## Conclusion
- Functions are the verbs of a domain-specific language within a system.
- Writing clear, concise, and well-named functions is essential for telling the story of the system effectively.