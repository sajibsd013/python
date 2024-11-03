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

Certainly! Here’s an example of each of the four core principles of Object-Oriented Programming (OOP): Encapsulation, Abstraction, Inheritance, and Polymorphism. Each example will include an explanation of the concept, code, and details.

---

### 1. Encapsulation
**Encapsulation** is the practice of bundling data (attributes) and methods (functions) within a class and restricting direct access to some components to protect the internal state.

Encapsulation is often achieved by making attributes private (with a preceding underscore or double underscore) and providing public getter and setter methods.

#### Example: Encapsulated Bank Account
```python
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.__balance  # Public method to access the private attribute

# Usage
account = BankAccount("Alice", 1000)
account.deposit(500)
print("Balance:", account.get_balance())
```

**Explanation**:
- The `__balance` attribute is private, meaning it can’t be accessed directly from outside the class.
- The `deposit`, `withdraw`, and `get_balance` methods are used to interact with `__balance` safely.
- This prevents direct modifications to `__balance`, ensuring data integrity and controlled access.

---

### 2. Abstraction
**Abstraction** is the concept of hiding the internal implementation details and exposing only the necessary parts of an object. In Python, abstraction is often achieved using abstract classes and methods, where only the essential details are defined, leaving specific implementations to subclasses.

#### Example: Abstract Payment System
```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# Usage
payment1 = CreditCardPayment()
payment1.process_payment(100)

payment2 = PayPalPayment()
payment2.process_payment(200)
```

**Explanation**:
- The `Payment` class is an abstract base class with an abstract method `process_payment`.
- `CreditCardPayment` and `PayPalPayment` inherit from `Payment` and provide their own implementations of `process_payment`.
- Users of the `Payment` class don’t need to know the specifics of how each payment is processed, achieving abstraction.

---

### 3. Inheritance
**Inheritance** allows a class (child class) to inherit attributes and methods from another class (parent class), promoting code reuse and a hierarchical structure.

#### Example: Inheritance in Vehicle Classes
```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Vehicle: {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def display_info(self):
        super().display_info()
        print(f"Doors: {self.doors}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, engine_cc):
        super().__init__(make, model)
        self.engine_cc = engine_cc

    def display_info(self):
        super().display_info()
        print(f"Engine: {self.engine_cc} cc")

# Usage
car = Car("Toyota", "Camry", 4)
motorcycle = Motorcycle("Harley-Davidson", "Iron 883", 883)

car.display_info()
motorcycle.display_info()
```

**Explanation**:
- `Vehicle` is the parent class with attributes `make` and `model` and a method `display_info`.
- `Car` and `Motorcycle` are child classes that inherit from `Vehicle` and add their own specific attributes (`doors` for `Car` and `engine_cc` for `Motorcycle`).
- Each subclass overrides the `display_info` method to include their additional information.
- This structure promotes reuse of common attributes and methods from `Vehicle` and allows subclasses to add their specific details.

---

### 4. Polymorphism
**Polymorphism** is the ability to use a single interface for different underlying forms (data types). In OOP, polymorphism allows you to define a method in the parent class, and each subclass can have a different implementation of that method.

#### Example: Polymorphic Animals
```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Chirp!"

# Usage
animals = [Dog(), Cat(), Bird()]
for animal in animals:
    print(animal.speak())
```

---

| OOP Concept        | Explanation                                                                                       | Code Example                    |
|--------------------|---------------------------------------------------------------------------------------------------|---------------------------------|
| **Encapsulation**  | Bundling data and methods inside a class, restricting direct access to certain attributes.       | Private attributes and getters. |
| **Abstraction**    | Hiding complex implementation details, exposing only what is necessary.                          | Abstract classes and methods.   |
| **Inheritance**    | Creating a new class based on an existing class, promoting code reuse and a class hierarchy.     | Parent and child classes.       |
| **Polymorphism**   | Using a single interface for different types, allowing methods to behave differently across types.| Method overriding in subclasses.|

These examples illustrate the key principles of OOP in Python, which can help in building organized, reusable, and scalable code. Each concept plays a crucial role in how object-oriented design supports effective software development.

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

### Summary
- **Procedural Approach**: Useful for simple, small-scale tasks but hard to maintain in complex applications.
- **Object-Oriented Approach**: Organizes data and behavior in classes, making code modular and easier to manage.

### _Happy learning!_


