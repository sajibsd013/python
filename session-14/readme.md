# Object-Oriented Programming (OOP) in Python

### 1. **Inheritance**
Inheritance allows one class (child class) to inherit attributes and methods from another class (parent class). It enables code reuse and creates a hierarchy.

### 2. **Exceptions**
Exceptions are runtime errors that disrupt normal program execution. Python provides mechanisms to handle exceptions using `try-except` blocks to make programs robust.

### 3. **Generators, Iterators, and Closures**
- **Generators**: Special functions that yield values one at a time, used for memory-efficient looping.
- **Iterators**: Objects that allow sequential access to elements using the `__iter__()` and `__next__()` methods.
- **Closures**: Functions that capture variables from their enclosing scope to maintain state between calls.

---

## Examples and Explanations

### 1. **Inheritance**

#### Example: Parent and Child Classes
```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Child class
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."

# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Buddy barks.
print(cat.speak())  # Whiskers meows.
```

#### Example: Using `super()`
```python
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)  # Call the parent constructor
        self.doors = doors

    def details(self):
        return f"{self.brand}, Year: {self.year}, Doors: {self.doors}"

car = Car("Toyota", 2020, 4)
print(car.details())  # Toyota, Year: 2020, Doors: 4
```

---

### 2. **Exceptions**

#### Example: Handling Exceptions
```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
else:
    print("No exceptions occurred.")
finally:
    print("Execution complete.")
```

#### Example: Custom Exceptions
```python
class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

# Raising a custom exception
try:
    raise CustomError("This is a custom error!")
except CustomError as e:
    print(f"Caught an error: {e}")
```

---

### 3. **Generators, Iterators, and Closures**

#### Example: Generators
```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # Yields the next value
        count += 1

# Using the generator
for number in count_up_to(5):
    print(number)
```

#### Example: Iterators
```python
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration

counter = Counter(3)
for num in counter:
    print(num)  # 1, 2, 3
```

#### Example: Closures
```python
def multiplier(factor):
    def multiply_by(x):
        return x * factor
    return multiply_by

# Create a closure
double = multiplier(2)
triple = multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

---


### _Happy learning!_


