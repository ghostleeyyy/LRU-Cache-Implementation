# LRU Cache in Python

An implementation of a Least Recently Used (LRU) Cache using a hash map and doubly linked list.

## Features

- Average O(1) lookup and update operations
- Automatic eviction of the least recently used entry
- Handles existing-key updates and zero capacity
- Includes test cases for core operations and eviction behavior

## Data Structures

The hash map provides direct access to cache nodes, while the doubly linked list maintains usage order and supports constant-time node updates.

## Run

```bash
python lru_cache.py
```

## Complexity

- `get`: Average O(1) time
- `put`: Average O(1) time
- Space: O(C), where C is the cache capacity

## Technologies

Python 3, Hash Map, Doubly Linked List