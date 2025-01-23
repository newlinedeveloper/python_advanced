## 𝗕𝗮𝘀𝗶𝗰: 𝗟𝗮𝘆𝗶𝗻𝗴 𝘁𝗵𝗲 𝗙𝗼𝘂𝗻𝗱𝗮𝘁𝗶𝗼𝗻

### **1. What is Python, and its key features?**
- Python is a high-level, interpreted programming language known for its simplicity and readability.
- **Key Features**:
  - Easy to learn and use.
  - Dynamically typed.
  - Extensive standard library.
  - Supports object-oriented and functional programming.
  - Platform-independent.
  - Rich in third-party libraries.

---

### **2. What are Python's built-in data types?**
- **Numeric Types**: `int`, `float`, `complex`
- **Sequence Types**: `list`, `tuple`, `range`
- **Text Type**: `str`
- **Set Types**: `set`, `frozenset`
- **Mapping Type**: `dict`
- **Boolean Type**: `bool`
- **Binary Types**: `bytes`, `bytearray`, `memoryview`
- **None Type**: `NoneType`

---

### **3. How do you declare and use variables in Python?**
- Variables are declared by assigning a value to a name:
  ```python
  x = 10  # Integer
  name = "Alice"  # String
  pi = 3.14  # Float
  ```

---

### **4. Explain the difference between a list, tuple, and set.**
- **List**: Ordered, mutable, allows duplicates.
  ```python
  lst = [1, 2, 3]
  ```
- **Tuple**: Ordered, immutable, allows duplicates.
  ```python
  tpl = (1, 2, 3)
  ```
- **Set**: Unordered, mutable, does not allow duplicates.
  ```python
  st = {1, 2, 3}
  ```

---

### **5. How do you iterate over a list in Python?**
- Using a `for` loop:
  ```python
  lst = [1, 2, 3]
  for item in lst:
      print(item)
  ```

---

### **6. What are Python’s conditional statements, and how are they used?**
- **Conditional Statements**: `if`, `elif`, `else`
  ```python
  x = 10
  if x > 5:
      print("Greater than 5")
  elif x == 5:
      print("Equal to 5")
  else:
      print("Less than 5")
  ```

---

### **7. How does Python handle memory management?**
- Python uses a **garbage collector** to manage memory.
- It relies on reference counting and cycles detection to clean unused objects.

---

### **8. Explain the use of the `len()` function.**
- Returns the number of items in a sequence or collection:
  ```python
  lst = [1, 2, 3]
  print(len(lst))  # Output: 3
  ```

---

### **9. What is the difference between `is` and `==` in Python?**
- `is`: Checks if two objects refer to the same memory location (identity).
- `==`: Checks if two objects have the same value (equality).
  ```python
  x = [1, 2, 3]
  y = [1, 2, 3]
  print(x is y)  # False
  print(x == y)  # True
  ```

---

### **10. How do you handle exceptions in Python?**
- Using `try`, `except`, `else`, and `finally` blocks:
  ```python
  try:
      x = 10 / 0
  except ZeroDivisionError as e:
      print(f"Error: {e}")
  ```

---

### **11. What are Python functions, and how do you define them?**
- Functions are reusable blocks of code defined using `def`:
  ```python
  def greet(name):
      return f"Hello, {name}!"
  print(greet("Alice"))
  ```

---

### **12. What is the difference between `*args` and `**kwargs`?**
- `*args`: Allows passing a variable number of positional arguments.
- `**kwargs`: Allows passing a variable number of keyword arguments.
  ```python
  def example(*args, **kwargs):
      print(args)
      print(kwargs)
  example(1, 2, key="value")
  ```

---

### **13. How is Python's `for` loop different from other programming languages?**
- Python's `for` loop iterates directly over items in an iterable, unlike C-style loops:
  ```python
  for item in [1, 2, 3]:
      print(item)
  ```

---

### **14. Explain the purpose of the `range()` function.**
- Generates a sequence of numbers:
  ```python
  for i in range(1, 5):
      print(i)  # Output: 1, 2, 3, 4
  ```

---

### **15. How do you import and use modules in Python?**
- Use `import` to include a module:
  ```python
  import math
  print(math.sqrt(16))  # Output: 4.0
  ```

---

### **16. What are Python decorators, and how do they work?**
- Decorators modify the behavior of functions or methods:
  ```python
  def decorator(func):
      def wrapper():
          print("Before function")
          func()
          print("After function")
      return wrapper

  @decorator
  def say_hello():
      print("Hello!")
  say_hello()
  ```

---

### **17. How do you reverse a string in Python?**
- Using slicing:
  ```python
  s = "hello"
  print(s[::-1])  # Output: "olleh"
  ```

---

### **18. How do you check if an element exists in a list?**
- Using the `in` operator:
  ```python
  lst = [1, 2, 3]
  print(2 in lst)  # Output: True
  ```

---

### **19. What is a lambda function? Provide an example.**
- A lambda function is an anonymous, single-expression function:
  ```python
  square = lambda x: x ** 2
  print(square(5))  # Output: 25
  ```

--- 

𝗜𝗻𝘁𝗲𝗿𝗺𝗲𝗱𝗶𝗮𝘁𝗲: Keep Practicing

### **1. Explain the difference between shallow copy and deep copy in Python.**
- **Shallow Copy**: Copies the top-level structure of an object, but nested objects are references.
  ```python
  import copy
  shallow = copy.copy(obj)
  ```
- **Deep Copy**: Copies all levels of the object, including nested objects.
  ```python
  deep = copy.deepcopy(obj)
  ```

---

### **2. What are Python comprehensions, and how are they used?**
- Python comprehensions provide a concise way to create lists, dictionaries, or sets.
  ```python
  # List comprehension
  squares = [x**2 for x in range(5)]
  ```

---

### **3. How does Python's garbage collection work?**
- Python uses **reference counting** and a **cyclic garbage collector** to clean up unused objects.
- Circular references are handled by detecting and breaking cycles.

---

### **4. Explain Python's Global Interpreter Lock (GIL).**
- GIL ensures only one thread executes Python bytecode at a time, limiting multi-threaded CPU-bound performance but allowing efficient I/O-bound tasks.

---

### **5. What is the difference between mutable and immutable objects in Python?**
- **Mutable**: Can be changed (e.g., `list`, `dict`).
- **Immutable**: Cannot be changed (e.g., `str`, `tuple`).

---

### **6. How do you use Python's zip() function?**
- Combines two or more iterables into tuples.
  ```python
  zipped = zip([1, 2], ['a', 'b'])
  print(list(zipped))  # [(1, 'a'), (2, 'b')]
  ```

---

### **7. Explain the difference between @staticmethod and @classmethod.**
- **`@staticmethod`**: A method that doesn’t access the class or instance.
- **`@classmethod`**: A method that takes the class (`cls`) as its first parameter.
  ```python
  class MyClass:
      @staticmethod
      def static_method(): pass
      @classmethod
      def class_method(cls): pass
  ```

---

### **8. How do you merge two dictionaries in Python?**
- **Python 3.9+**: Use the `|` operator:
  ```python
  merged = dict1 | dict2
  ```

---

### **9. What is the difference between sort() and sorted()?**
- **`sort()`**: Modifies the original list in place.
- **`sorted()`**: Returns a new sorted list.
  ```python
  lst.sort()
  sorted(lst)
  ```

---

### **10. How do you handle file operations in Python?**
- Use the built-in `open()` function.
  ```python
  with open('file.txt', 'r') as file:
      content = file.read()
  ```

---

### **11. What are Python's iterators and generators?**
- **Iterators**: Objects that implement `__iter__` and `__next__`.
- **Generators**: Functions that use `yield` to lazily produce values.
  ```python
  def gen():
      yield 1
      yield 2
  ```

---

### **12. How do you use the `with` statement in Python?**
- Simplifies resource management (e.g., file handling) by automatically closing resources.
  ```python
  with open('file.txt', 'r') as file:
      data = file.read()
  ```

---

### **13. What is Python's itertools module, and when would you use it?**
- **`itertools`** provides tools for efficient iteration like `product`, `permutations`, `combinations`.
  ```python
  from itertools import permutations
  print(list(permutations([1, 2, 3], 2)))
  ```

---

### **14. Explain the difference between positional and keyword arguments.**
- **Positional**: Passed based on their position.
- **Keyword**: Passed with a key-value pair.
  ```python
  def func(a, b): pass
  func(1, b=2)
  ```

---

### **15. How do you perform matrix operations in Python?**
- Use **NumPy** for matrix operations.
  ```python
  import numpy as np
  a = np.array([[1, 2], [3, 4]])
  b = np.array([[5, 6], [7, 8]])
  print(np.dot(a, b))
  ```

---

### **16. What are Python's metaclasses, and how are they used?**
- Metaclasses control the behavior of class creation.
  ```python
  class Meta(type):
      def __new__(cls, name, bases, dct):
          return super().__new__(cls, name, bases, dct)

  class MyClass(metaclass=Meta):
      pass
  ```

---

### **17. How do you perform unit testing in Python?**
- Use the `unittest` module.
  ```python
  import unittest

  class TestExample(unittest.TestCase):
      def test_case(self):
          self.assertEqual(1 + 1, 2)
  ```

---

### **18. Explain how Python's `os` module is used.**
- The `os` module allows interaction with the operating system.
  ```python
  import os
  os.mkdir('new_folder')
  ```

---

### **19. What are Python's `argsort()` and `argmax()` functions?**
- **`argsort()`**: Returns indices that would sort the array.
- **`argmax()`**: Returns the index of the maximum value.

---

### **20. How do you optimize code performance in Python?**
- Use libraries like NumPy, PyPy, and Cython.
- Profile the code with tools like `cProfile`.
- Avoid unnecessary loops and use efficient data structures.

---

𝗔𝗱𝘃𝗮𝗻𝗰𝗲𝗱: 𝗧𝗮𝗸𝗶𝗻𝗴 𝗬𝗼𝘂𝗿 𝗦𝗸𝗶𝗹𝗹𝘀 𝗧𝗼 𝗧𝗵𝗲 𝗡𝗲𝘅𝘁 𝗟𝗲𝘃𝗲𝗹

---

### **1. How does Python's multiprocessing differ from threading?**
- **Multiprocessing**: 
  - Uses separate processes, each with its own memory space.
  - Bypasses the **Global Interpreter Lock (GIL)**, allowing true parallelism.
  - Suitable for CPU-bound tasks.
- **Threading**:
  - Uses threads within the same process, sharing memory.
  - Limited by the GIL, so it doesn’t achieve true parallelism for CPU-bound tasks.
  - Suitable for I/O-bound tasks.

---

### **2. Explain how to implement a custom Python metaclass.**
A **metaclass** defines how classes behave.

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

# Output: Creating class MyClass
```

---

### **3. How do you implement memoization in Python?**
Memoization stores results of expensive function calls for reuse.

```python
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
```

---

### **4. What is Python's asyncio, and how does it handle concurrency?**
- **`asyncio`** is a library for writing asynchronous programs using `async` and `await`.
- It uses an **event loop** to handle concurrency, enabling I/O-bound tasks to execute without blocking.

Example:
```python
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(say_hello())
```

---

### **5. How do you profile Python code to identify performance bottlenecks?**
Use the built-in **`cProfile`** module to analyze performance.

```bash
python -m cProfile -s time your_script.py
```

Example:
```python
import cProfile
cProfile.run("sum(range(1000))")
```

---

### **6. How do you handle circular imports in Python projects?**
- **Use import statements inside functions** to delay loading.
- **Refactor code** to avoid circular dependencies by moving shared functionality to a separate module.
- Example:
  ```python
  def func():
      from module_b import some_function
      some_function()
  ```

---

### **7. What are Python’s weak references, and when would you use them?**
- **Weak references** (in `weakref` module) allow referencing objects without preventing them from being garbage collected.
- Used for caching or monitoring object lifetimes.

Example:
```python
import weakref

class MyClass:
    pass

obj = MyClass()
weak_ref = weakref.ref(obj)

print(weak_ref())  # Access the object
del obj
print(weak_ref())  # None (object is garbage collected)
```

---

### **8. How do you implement a binary search algorithm in Python?**

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search([1, 2, 3, 4, 5], 4))  # Output: 3
```

---

### **9. How does Python's dataclasses module work, and when should you use it?**
- `dataclasses` simplifies the creation of classes with minimal boilerplate.
- Automatically generates `__init__`, `__repr__`, and comparison methods.

Example:
```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(10, 20)
print(p)  # Output: Point(x=10, y=20)
```

---

### **10. What are Python's context managers, and how do you create a custom one?**
- **Context managers** ensure proper resource management (e.g., closing files).
- Use the `with` statement or create a custom context manager.

**Custom Context Manager**:
```python
class MyContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")

with MyContext() as ctx:
    print("Inside context")
```

Output:
```
Entering context
Inside context
Exiting context
```

---
