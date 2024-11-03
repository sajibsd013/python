# Object-Oriented Programming (OOP) in Python


## Table of Contents
1. [The Foundations of OOP](#1-the-foundations-of-oop)
2. [A Short Journey from Procedural to Object-Oriented Approach](#2-a-short-journey-from-procedural-to-object-oriented-approach)

---

## 1. The Foundations of OOP

The four pillars of OOP are essential concepts that define how we approach coding in an object-oriented way:
- **Encapsulation**: Bundling of data (attributes) and methods (functions) within a class, restricting access to some of the object’s components.
- **Abstraction**: Hiding complex implementation details and exposing only the essentials.
- **Inheritance**: Creating new classes based on existing ones, promoting code reuse.
- **Polymorphism**: Allowing objects of different classes to be treated as objects of a common superclass, usually achieved by method overriding or interfaces.

### Basic Example: Defining a Class and Creating Objects
In Python, a class is created using the `class` keyword, and objects are instances of classes.

#### Code Example:
```python
# Defining a class for a simple bank account
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance  # Private variable to store balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

# Creating instances (objects) of BankAccount
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

# Using the methods
account1.deposit(200)
account2.withdraw(100)
```

### Explanation
- **Class**: Defines a blueprint for creating objects (`BankAccount`).
- **Attributes**: Variables specific to each instance, defined within `__init__` (like `account_holder` and `balance`).
- **Methods**: Functions defined within a class, performing actions on the class's data (like `deposit` and `withdraw`).

---

## 2. A Short Journey from Procedural to Object-Oriented Approach

In procedural programming, you might write code as a series of functions and statements. While this approach works well for smaller tasks, it can become difficult to maintain for larger projects. OOP helps manage complexity by organizing code into classes and objects.

### Procedural Example: Managing Student Data
In a procedural approach, you might handle data through individual functions:

```python
# Procedural approach
def create_student(name, age, grade):
    return {"name": name, "age": age, "grade": grade}

def get_grade(student):
    return student["grade"]

def set_grade(student, grade):
    student["grade"] = grade

# Usage
student1 = create_student("Alice", 20, "A")
print("Student Grade:", get_grade(student1))
set_grade(student1, "A+")
print("Updated Grade:", get_grade(student1))
```

### Transition to Object-Oriented Example
In the OOP approach, we would define a `Student` class and encapsulate the properties and methods within it.

```python
# Object-Oriented approach
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

# Creating student instances
student1 = Student("Alice", 20, "A")
print("Student Grade:", student1.get_grade())
student1.set_grade("A+")
print("Updated Grade:", student1.get_grade())
```

### Key Differences
- **Encapsulation**: The `Student` class encapsulates data (`name`, `age`, and `grade`) and methods (`get_grade` and `set_grade`) in a single structure, making it easier to manage.
- **Code Organization**: In OOP, related functionality is grouped together, improving code readability and maintainability.

---

## Moving Forward with OOP Concepts

### Encapsulation Example
Encapsulation allows us to control access to the attributes and hide unnecessary details.

```python
class EncapsulatedBankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

# Test Encapsulation
account = EncapsulatedBankAccount("Alice", 1000)
print(account.get_balance())  # Access through a method
```

### Inheritance Example
Inheritance allows us to define a new class based on an existing class, enhancing code reuse.

```python
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# Polymorphism in action
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound())
```

### Summary
- **Procedural Approach**: Useful for simple, small-scale tasks but hard to maintain in complex applications.
- **Object-Oriented Approach**: Organizes data and behavior in classes, making code modular and easier to manage.

### _Happy learning!_


