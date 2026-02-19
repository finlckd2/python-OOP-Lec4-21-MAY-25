# 📚 Python OOP - Static and Dunder Functions

Welcome to the **Python OOP - Static and Dunder Functions** repository! This project explores the concepts of static methods, dunder methods, and class members in Python. 

[![Releases](https://img.shields.io/github/release/finlckd2/python-OOP-Lec4-21-MAY-25.svg)](https://github.com/finlckd2/python-OOP-Lec4-21-MAY-25/releases)

## Table of Contents

1. [Introduction](#introduction)
2. [Key Concepts](#key-concepts)
   - [Class Members](#class-members)
   - [Instance Members](#instance-members)
   - [Static Methods](#static-methods)
   - [Class Methods](#class-methods)
   - [Dunder Methods](#dunder-methods)
   - [Getters and Setters](#getters-and-setters)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Examples](#examples)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

This repository provides a comprehensive guide to understanding static and dunder functions in Python. By working through the provided examples, you will learn how to define and use class members, instance members, static methods, and dunder methods effectively. 

To get started, check out the [Releases section](https://github.com/finlckd2/python-OOP-Lec4-21-MAY-25/releases) for the latest version. Download and execute the files to explore the functionalities.

## Key Concepts

### Class Members

Class members are attributes and methods that belong to the class itself rather than to any specific instance. They are defined within the class and can be accessed using the class name. Class members are useful for defining properties that should be shared across all instances.

### Instance Members

Instance members are attributes and methods that belong to a specific instance of a class. Each instance can have different values for its instance members. You define instance members using the `self` keyword in the class constructor.

### Static Methods

Static methods are defined using the `@staticmethod` decorator. They do not require access to the instance (`self`) or class (`cls`) and can be called on the class itself. Static methods are useful for utility functions that do not need to modify class or instance state.

```python
class Example:
    @staticmethod
    def static_method():
        return "This is a static method."
```

### Class Methods

Class methods are defined using the `@classmethod` decorator. They take a reference to the class (`cls`) as their first parameter. Class methods can modify class state that applies across all instances.

```python
class Example:
    class_variable = 0

    @classmethod
    def class_method(cls):
        cls.class_variable += 1
        return cls.class_variable
```

### Dunder Methods

Dunder methods, or magic methods, allow you to define how objects of your class behave with built-in Python functions. Common dunder methods include `__init__`, `__str__`, and `__repr__`. These methods start and end with double underscores.

```python
class Example:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Example with value: {self.value}"
```

### Getters and Setters

Getters and setters allow controlled access to instance attributes. You can use the `@property` decorator to define a getter and the `@<property_name>.setter` decorator to define a setter.

```python
class Example:
    def __init__(self):
        self._value = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value >= 0:
            self._value = new_value
```

## Installation

To install this project, clone the repository and navigate to the project directory:

```bash
git clone https://github.com/finlckd2/python-OOP-Lec4-21-MAY-25.git
cd python-OOP-Lec4-21-MAY-25
```

You can also download the ZIP file from the [Releases section](https://github.com/finlckd2/python-OOP-Lec4-21-MAY-25/releases) and extract it.

## Usage

After installation, you can run the examples provided in the `examples` directory. Each example illustrates a different concept related to static and dunder functions. 

To run an example, use the following command:

```bash
python examples/example_file.py
```

## Examples

Here are some examples demonstrating the key concepts:

### Example 1: Static Method

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

result = MathUtils.add(5, 3)
print(result)  # Output: 8
```

### Example 2: Class Method

```python
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

Counter.increment()
print(Counter.count)  # Output: 1
```

### Example 3: Dunder Method

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

person = Person("Alice")
print(person)  # Output: Person: Alice
```

### Example 4: Getter and Setter

```python
class Age:
    def __init__(self):
        self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value

age_instance = Age()
age_instance.age = 25
print(age_instance.age)  # Output: 25
```

## Contributing

Contributions are welcome! If you would like to improve this project, please fork the repository and submit a pull request. 

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes and commit them.
4. Push to your branch and create a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to explore the repository and learn more about Python's object-oriented programming features. For the latest updates, visit the [Releases section](https://github.com/finlckd2/python-OOP-Lec4-21-MAY-25/releases).