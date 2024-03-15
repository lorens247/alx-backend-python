# 0x00 - Python - Variable Annotations

## Overview

This guide covers Python variable annotations, a feature introduced in Python 3 to specify types for variables and function signatures. It discusses how to use type annotations, the concept of duck typing, and validating code using mypy.

## Contents

- **Type Annotations in Python 3**: Explanation of type annotations and their significance in Python 3.
- **Using Type Annotations**: How to use type annotations to specify function signatures and variable types.
- **Duck Typing**: Understanding the concept of duck typing and its relationship with type annotations.
- **Validating Code with Mypy**: Introduction to mypy, a static type checker for Python, and how to use it to validate code.

## Key Concepts

- **Type Annotations**: Annotations used to specify types for variables and function arguments in Python 3.
- **Function Signatures**: Describing the types of arguments and return values of functions using type annotations.
- **Duck Typing**: A programming concept where the type or the class of an object is less important than the methods it defines.
- **Mypy**: A static type checker for Python that analyzes code and detects type-related errors.

## How to Use

1. Define variable annotations using the syntax `variable_name: type`.
2. Specify function signatures using type annotations for parameters and return types.
3. Utilize duck typing by focusing on the object's behavior rather than its type.
4. Validate your code using mypy by running it against your Python files.

## Resources

- [Type Annotations (Python Documentation)](https://docs.python.org/3/library/typing.html)
- [Mypy Documentation](https://mypy.readthedocs.io/en/stable/)

## Example

```python
from typing import List

def process_numbers(numbers: List[int]) -> int:
    """
    Returns the sum of a list of integers.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        int: The sum of the integers in the list.
    """
    return sum(numbers)

# Example usage
result = process_numbers([1, 2, 3, 4])
print(result)  # Output: 10
