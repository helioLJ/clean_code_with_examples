# Clean Code - Chapter 6 Summary: Objects and Data Structures

## Objects and Data Structures

### Data Abstraction
- **Encapsulation**: Keep variables private to allow changes without affecting external code. Avoid exposing private variables through getters and setters.
- **Abstract Interfaces**: Use abstract interfaces to manipulate data without revealing implementation details. This allows flexibility in changing the underlying data representation.

### Data/Object Anti-Symmetry
- **Objects vs. Data Structures**: 
  - Objects hide data and expose behavior through methods.
  - Data structures expose data and have little or no behavior.
- **Trade-offs**:
  - Procedural code (data structures) makes it easy to add new functions but hard to add new data types.
  - Object-oriented code makes it easy to add new data types but hard to add new functions.

### The Law of Demeter
- **Principle**: A module should not know about the internal details of the objects it manipulates. It should only interact with its immediate "friends" (objects it directly knows).
- **Train Wrecks**: Avoid long chains of method calls that expose the internal structure of objects.

### Hybrids
- **Avoid Hybrid Structures**: Do not mix objects and data structures. Hybrids make it difficult to add new functions and data types.

### Hiding Structure
- **Encapsulation**: Objects should encapsulate their behavior and not expose their internal structure. Use methods that perform actions rather than exposing data for manipulation.

### Data Transfer Objects (DTOs)
- **Definition**: DTOs are simple data structures with public variables and no behavior. They are useful for transferring data between systems.
- **Beans**: A form of DTO with private variables and getters/setters, offering minimal encapsulation.

### Active Record
- **Definition**: A special form of DTO that includes methods for database operations like `save` and `find`.
- **Separation of Concerns**: Keep business logic separate from data structures to avoid creating hybrids.

### Conclusion
- **Objects**: Expose behavior and hide data, making it easy to add new types but hard to add new behaviors.
- **Data Structures**: Expose data and have little behavior, making it easy to add new behaviors but hard to add new types.
- **Balance**: Choose the right approach based on whether you need to add new data types or new behaviors.
