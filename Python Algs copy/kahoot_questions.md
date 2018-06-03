## Kahoot Questions

Q 1) What is the runtime complexity of this algorithm?

```python
def sum_nums(n):
    total_sum = 0
    for _ in range(n):
        for _ in range(n):
            total_sum += 1
            
    return total_sum
```

Q 2) What is the runtime complexity of this algorithm?
```python
def sum_more_nums(n):
    total_sum = 0
    for _ in range(100):
        total_sum += 1

    for _ in range(100):
        total_sum += 1
     
    return total_sum
```

Q 3) What does this code print?
```python
for _ in range(100);
    for _ in range(100);
        for _ in range(100);
            for _ in range(100);
                for _ in range(100);
                    n += 1

print(n)

```

Q 4) What is the big O complexity for this algorithm?
```python
def binary_search(array, to_find):
    """ Check if to_find is in array and return the index of it.
    If not in the array, return None.
    """
    offset = 0
    while len(array) >= 1:
        idx = len(array) // 2
        if array[idx] == to_find:
            return idx + offset
        
        if array[idx] < to_find:
            offset += idx
            array = array[idx:]
        else:
            array = array[:idx]
        
    return None
```
