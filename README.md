# python_advanced
Python Advanced programming concepts

- Magic Methods & Dunder
- Decorators
- Generators
- Argument parsing
- Encapsulation
- Type hinting
- Factory design pattern
- Proxy design pattern
- singleton design pattern
- composite design pattern


### 1. Magic Methods & Dunder Methods
Magic methods (also known as dunder methods because they start and end with double underscores) allow you to define how objects of your classes behave with built-in Python operations (like `+`, `-`, `len()`, etc.).

**Example:**

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)  # Output: Point(4, 6)
```

### 2. Decorators
Decorators are a way to modify or enhance functions or methods without changing their actual code.

**Example:**

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

### 3. Generators
Generators are a way to create iterators in a more memory-efficient way using `yield` instead of `return`.

**Example:**

```python
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

for number in count_up_to(5):
    print(number)
```

### 4. Argument Parsing
Argument parsing is used to handle command-line arguments in Python scripts.

**Example:**

```python
import argparse

parser = argparse.ArgumentParser(description="A simple example script")
parser.add_argument("name", help="Your name")
parser.add_argument("-a", "--age", type=int, help="Your age")
args = parser.parse_args()

print(f"Hello, {args.name}!")
if args.age:
    print(f"You are {args.age} years old.")
```

### 5. Encapsulation
Encapsulation is the bundling of data and methods that operate on the data within one unit, e.g., a class in Python.

**Example:**

```python
class Person:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age    # private attribute

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

person = Person("John", 30)
print(person.get_name())
print(person.get_age())
```

### 6. Type Hinting
Type hinting provides a way to specify the types of variables, function arguments, and return values.

**Example:**

```python
def greeting(name: str) -> str:
    return 'Hello ' + name

print(greeting("Alice"))
```

### 7. Factory Design Pattern
The Factory Design Pattern is a creational pattern that provides a way to create objects without specifying the exact class of object that will be created.

**Example:**

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def get_pet(pet_type: str):
    pets = {"dog": Dog, "cat": Cat}
    return pets[pet_type]()

pet = get_pet("dog")
print(pet.speak())
```

### 8. Proxy Design Pattern
The Proxy Design Pattern is used to provide a surrogate or placeholder for another object to control access to it.

**Example:**

```python
class RealSubject:
    def request(self):
        return "RealSubject: Handling request."

class Proxy:
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self):
        print("Proxy: Checking access prior to firing a real request.")
        return self._real_subject.request()

real_subject = RealSubject()
proxy = Proxy(real_subject)
print(proxy.request())
```

### 9. Singleton Design Pattern
The Singleton Design Pattern ensures that a class has only one instance and provides a global point of access to it.

**Example:**

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # Output: True
```

### 10. Composite Design Pattern
The Composite Design Pattern allows you to compose objects into tree structures to represent part-whole hierarchies.

**Example:**

```python
class Component:
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, component):
        self._children.append(component)

    def operation(self):
        results = []
        for child in self._children:
            results.append(child.operation())
        return " + ".join(results)

leaf = Leaf()
composite = Composite()
composite.add(leaf)
composite.add(Leaf())
print(composite.operation())
```

Sure! Let's dive into these advanced Python concepts with explanations and examples:

### **1. Decorators**
Decorators are a way to modify the behavior of a function or class method. They are often used to add functionality such as logging, access control, or caching without modifying the original function code.

**Example:**

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@decorator
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

**Output:**
```
Calling greet with ('Alice',) and {}
Hello, Alice!
```

### **2. Context Managers**
Context managers are used to manage resources, such as file handling or database connections, ensuring proper acquisition and release of resources.

**Example using `with` statement:**

```python
with open('file.txt', 'w') as file:
    file.write('Hello, world!')
```

Here, the `with` statement ensures that the file is properly closed after writing, even if an error occurs.

**Custom Context Manager:**

```python
class MyContext:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

with MyContext() as context:
    print("Inside the context")
```

**Output:**
```
Entering the context
Inside the context
Exiting the context
```

### **3. Metaclasses**
A metaclass is a class of a class that defines how a class behaves. A class is an instance of a metaclass, just as an object is an instance of a class.

**Example:**

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass
```

**Output:**
```
Creating class MyClass
```

### **4. Asynchronous Programming**
Asynchronous programming allows you to perform non-blocking operations using `async` and `await`. This is particularly useful for I/O-bound and high-level structured network code.

**Example with `asyncio`:**

```python
import asyncio

async def greet(name):
    await asyncio.sleep(1)
    print(f"Hello, {name}!")

async def main():
    await asyncio.gather(greet("Alice"), greet("Bob"), greet("Charlie"))

asyncio.run(main())
```

**Output (after 1 second):**
```
Hello, Alice!
Hello, Bob!
Hello, Charlie!
```

