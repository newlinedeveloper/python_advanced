Sure! Below is an **LRU (Least Recently Used) Cache** implementation in **Python** using `OrderedDict` from the `collections` module and a **manual implementation** using a **doubly linked list** and a **hash map**.

---

## **🔹 What is an LRU Cache?**
- **LRU Cache** is a data structure that stores a **fixed number** of items.
- When the cache is full, **the least recently used item is removed**.
- It supports:
  - **O(1) Get**: Fetching a value should be fast.
  - **O(1) Put**: Adding or updating a value should be fast.

---

## **✅ Solution 1: Simple Implementation using `OrderedDict`**
Python’s `OrderedDict` maintains the **insertion order**, making it perfect for LRU.

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()  # Maintains order of insertion
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1  # Key not found
        
        # Move accessed item to end to mark as most recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)  # Move to end since it's recently used
        
        self.cache[key] = value  # Insert or update the key
        
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove least recently used item (first element)

# Example Usage
lru = LRUCache(3)
lru.put(1, "A")
lru.put(2, "B")
lru.put(3, "C")
print(lru.get(2))  # Output: "B"
lru.put(4, "D")  # Evicts key 1
print(lru.get(1))  # Output: -1 (Not found)
```

### **🔹 Why Use `OrderedDict`?**
- `move_to_end(key)`: Moves accessed key to the **end** (most recently used).
- `popitem(last=False)`: Removes the **first inserted key** (least recently used).
- **Time Complexity:** `O(1)` for both `get()` and `put()`.

---

## **✅ Solution 2: Manual Implementation (Doubly Linked List + Hash Map)**
To **avoid using `OrderedDict`**, we use:
- **Doubly Linked List**: Maintains order (Most → Least recently used).
- **Hash Map (`dict`)**: Stores key → Node reference for `O(1)` lookup.

### **🔹 Implementation**
```python
class Node:
    """Doubly Linked List Node"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Key -> Node lookup
        self.head = Node(0, 0)  # Dummy head (Most Recently Used)
        self.tail = Node(0, 0)  # Dummy tail (Least Recently Used)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Removes a node from the doubly linked list"""
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def _add_to_front(self, node):
        """Adds a node right after head (Most Recently Used)"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)  # Move accessed node to front
        self._add_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])  # Remove existing node
        
        node = Node(key, value)
        self.cache[key] = node
        self._add_to_front(node)

        if len(self.cache) > self.capacity:
            lru = self.tail.prev  # Least Recently Used node
            self._remove(lru)
            del self.cache[lru.key]  # Remove from hash map

# Example Usage
lru = LRUCache(3)
lru.put(1, "A")
lru.put(2, "B")
lru.put(3, "C")
print(lru.get(2))  # Output: "B"
lru.put(4, "D")  # Evicts key 1
print(lru.get(1))  # Output: -1 (Not found)
```

---

## **🔹 How It Works**
1. **Doubly Linked List:**  
   - **Head (Most Recently Used)** → **Tail (Least Recently Used)**
   - When a key is accessed, **move it to the front**.
   - When inserting a new key, **add it to the front**.
   - If cache is full, **remove the tail** (Least Recently Used).

2. **Hash Map:**  
   - Stores `{key: Node}` for **O(1) access**.

---

## **🔹 Complexity Analysis**
| Operation | `OrderedDict` Approach | Manual (DLL + Hash Map) Approach |
|-----------|------------------------|----------------------------------|
| **Get()** | `O(1)` | `O(1)` |
| **Put()** | `O(1)` | `O(1)` |
| **Remove LRU** | `O(1)` | `O(1)` |
| **Space Complexity** | `O(capacity)` | `O(capacity)` |

---

## **🚀 Summary**
| Approach | Pros | Cons |
|----------|------|------|
| **`OrderedDict`** | ✅ Simple, Built-in `O(1)` operations | ❌ Uses built-in library |
| **DLL + Hash Map** | ✅ Custom LRU logic, `O(1)` operations | ❌ More code complexity |

Sure! Let's **visualize** how the **LRU Cache** works step by step using a **Doubly Linked List + Hash Map** approach.

---

## **✅ LRU Cache Initialization**
- **Capacity:** `3`
- **Doubly Linked List (DLL) Structure:**
  ```
  HEAD <-> TAIL
  ```

- **Hash Map (`cache`):**
  ```
  {}
  ```

---

### **🔹 Step 1: `lru.put(1, "A")`**
- Insert `(1, "A")` into the **cache**.
- Move to the **front** of the DLL.

#### **📌 Hash Map (`cache`):**
```
{ 1: Node(1, "A") }
```

#### **📌 Doubly Linked List (DLL):**
```
HEAD <-> (1, "A") <-> TAIL
```

---

### **🔹 Step 2: `lru.put(2, "B")`**
- Insert `(2, "B")` into the **cache**.
- Move to the **front**.

#### **📌 Hash Map (`cache`):**
```
{ 1: Node(1, "A"), 2: Node(2, "B") }
```

#### **📌 DLL:**
```
HEAD <-> (2, "B") <-> (1, "A") <-> TAIL
```
- `(2, "B")` is **most recently used**.

---

### **🔹 Step 3: `lru.put(3, "C")`**
- Insert `(3, "C")` into the **cache**.
- Move to the **front**.

#### **📌 Hash Map (`cache`):**
```
{ 1: Node(1, "A"), 2: Node(2, "B"), 3: Node(3, "C") }
```

#### **📌 DLL:**
```
HEAD <-> (3, "C") <-> (2, "B") <-> (1, "A") <-> TAIL
```
- `(3, "C")` is **most recently used**.

---

### **🔹 Step 4: `lru.get(2)` → Returns `"B"`**
- Move `(2, "B")` to the **front**.

#### **📌 Hash Map (`cache`):**
```
{ 1: Node(1, "A"), 2: Node(2, "B"), 3: Node(3, "C") }
```

#### **📌 DLL (After Moving 2 to Front):**
```
HEAD <-> (2, "B") <-> (3, "C") <-> (1, "A") <-> TAIL
```
- **Most Recently Used:** `(2, "B")`
- **Least Recently Used (LRU):** `(1, "A")`

---

### **🔹 Step 5: `lru.put(4, "D")` (Cache Full, Remove LRU `(1, "A")`)**
- Remove `(1, "A")` (Least Recently Used).
- Insert `(4, "D")` at **front**.

#### **📌 Hash Map (`cache`):**
```
{ 2: Node(2, "B"), 3: Node(3, "C"), 4: Node(4, "D") }  # Removed 1
```

#### **📌 DLL:**
```
HEAD <-> (4, "D") <-> (2, "B") <-> (3, "C") <-> TAIL
```
- **Evicted:** `(1, "A")`
- **Most Recently Used:** `(4, "D")`
- **Least Recently Used (LRU):** `(3, "C")`

---

### **🔹 Step 6: `lru.get(1)` → Returns `-1` (Not Found)**
- **Key `1` was evicted**, so it **returns `-1`**.

#### **📌 Hash Map (`cache`):**
```
{ 2: Node(2, "B"), 3: Node(3, "C"), 4: Node(4, "D") }  # 1 is not found
```

#### **📌 DLL (No Change):**
```
HEAD <-> (4, "D") <-> (2, "B") <-> (3, "C") <-> TAIL
```

---

## **📌 Summary of LRU Operations**
| Step | Operation | Cache (`cache`) | DLL State (`HEAD <-> ... <-> TAIL`) |
|------|------------|----------------|-------------------------------------|
| 1 | `put(1, "A")` | `{1: A}` | `(1, A)` |
| 2 | `put(2, "B")` | `{1: A, 2: B}` | `(2, B) <-> (1, A)` |
| 3 | `put(3, "C")` | `{1: A, 2: B, 3: C}` | `(3, C) <-> (2, B) <-> (1, A)` |
| 4 | `get(2)` | `{1: A, 2: B, 3: C}` | `(2, B) <-> (3, C) <-> (1, A)` |
| 5 | `put(4, "D")` | `{2: B, 3: C, 4: D}` | `(4, D) <-> (2, B) <-> (3, C)` |
| 6 | `get(1)` | `{2: B, 3: C, 4: D}` | **No change** (1 is removed) |

---

## **🚀 Key Takeaways**
1. **Doubly Linked List (DLL)**:
   - Maintains **most-recently used → least-recently used** order.
   - **Head** = Most recently used (MRU).
   - **Tail** = Least recently used (LRU).

2. **Hash Map (`cache`)**:
   - Stores `{key → Node}` for **O(1) lookup**.
   - Removes least recently used items when capacity exceeds.

3. **Operations Complexity**:
   | Operation | Time Complexity |
   |-----------|----------------|
   | `get(key)` | `O(1)` |
   | `put(key, value)` | `O(1)` |
