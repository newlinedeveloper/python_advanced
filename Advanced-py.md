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
- Explain the difference between shallow copy and deep copy in Python.
- What are Python comprehensions, and how are they used?
- How does Python's garbage collection work?
- Explain Python's Global Interpreter Lock (GIL).
- What is the difference between mutable and immutable objects in Python?
- How do you use Python's zip() function?
- Explain the difference between @staticmethod and @classmethod.
- How do you merge two dictionaries in Python?
- What is the difference between sort() and sorted()?
- How do you handle file operations in Python?
- What are Python's iterators and generators?
- How do you use the with statement in Python?
- What is Python's itertools module, and when would you use it?
- Explain the difference between positional and keyword arguments.
- How do you perform matrix operations in Python?
- What are Python's metaclasses, and how are they used?
- How do you perform unit testing in Python?
- Explain how Python's os module is used.
- What are Python's argsort() and argmax() functions?
- How do you optimize code performance in Python?

𝗔𝗱𝘃𝗮𝗻𝗰𝗲𝗱: 𝗧𝗮𝗸𝗶𝗻𝗴 𝗬𝗼𝘂𝗿 𝗦𝗸𝗶𝗹𝗹𝘀 𝗧𝗼 𝗧𝗵𝗲 𝗡𝗲𝘅𝘁 𝗟𝗲𝘃𝗲𝗹
- How does Python's multiprocessing differ from threading?
- Explain how to implement a custom Python metaclass.
- How do you implement memoization in Python?
- What is Python's asyncio, and how does it handle concurrency?
- How do you profile Python code to identify performance bottlenecks?
- How do you handle circular imports in Python projects?
- What are Python’s weak references, and when would you use them?
- How do you implement a binary search algorithm in Python?
- How does Python's dataclasses module work, and when should you use it?
- What are Python's context managers, and how do you create a custom one?
