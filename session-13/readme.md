# Object-Oriented Programming (OOP) in Python

## Key Concepts in OOP

### 1. **OOP Properties**
Properties are the attributes or data members of a class. They define the characteristics of an object created from the class.  

### 2. **OOP Methods**
Methods are the functions defined within a class. They define the behaviors or actions of an object created from the class.  

---

## Understanding OOP with Examples

### Step 1: Define a Class with Properties and Methods

Below is an example using a `Car` class:

```python
class Car:
    # Constructor to initialize properties
    def __init__(self, brand, model, year):
        self.brand = brand  # Public property
        self.model = model  # Public property
        self.year = year    # Public property

    # Method to display car details
    def display_details(self):
        return f"{self.brand} {self.model}, Year: {self.year}"

    # Method to calculate car's age
    def calculate_age(self, current_year):
        return current_year - self.year

# Creating an object (an instance of the Car class)
my_car = Car("Toyota", "Corolla", 2015)

# Accessing properties
print("Brand:", my_car.brand)
print("Model:", my_car.model)
print("Year:", my_car.year)

# Calling methods
print("Details:", my_car.display_details())
print("Car Age:", my_car.calculate_age(2024))
```

---

### Step 2: Access Modifiers for Properties

In OOP, properties can have different access levels: **public**, **protected**, and **private**.

#### Example: Access Levels
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner            # Public property
        self._balance = balance       # Protected property
        self.__bank_code = "XYZ123"   # Private property

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount}, New Balance: ${self._balance}"
        return "Invalid amount"

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return f"Withdrew ${amount}, Remaining Balance: ${self._balance}"
        return "Insufficient balance or invalid amount"

# Creating an instance of BankAccount
account = BankAccount("John Doe", 1000)

# Accessing public and protected properties
print("Owner:", account.owner)
print("Balance:", account.get_balance())

# Accessing private property (raises AttributeError)
# print(account.__bank_code)

# Using methods
print(account.deposit(500))
print(account.withdraw(300))
```

---

### Step 3: Special Methods (Magic Methods)

Special methods in Python (also called magic methods) add custom behavior to objects.

#### Example: Customizing String Representation
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, Age: {self.age}"

# Creating an object
person = Person("Alice", 30)
print(person)  # Output: Alice, Age: 30
```

---

### _Happy learning!_


