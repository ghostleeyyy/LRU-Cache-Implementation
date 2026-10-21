class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        if isinstance(capacity, bool) or not isinstance(capacity, int):
            raise TypeError("Capacity must be an integer.")
        if capacity < 0:
            raise ValueError("Capacity cannot be negative.")

        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        node = self.cache.get(key)

        if node is None:
            return -1

        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
            return

        node = Node(key, value)
        self.cache[key] = node
        self._add_to_front(node)

        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]


def test_lru_cache():
    cache = LRUCache(2)

    cache.put(1, 10)
    cache.put(2, 20)
    assert cache.get(1) == 10

    cache.put(3, 30)
    assert cache.get(2) == -1

    cache.put(4, 40)
    assert cache.get(1) == -1
    assert cache.get(3) == 30
    assert cache.get(4) == 40

    cache.put(4, 45)
    assert cache.get(4) == 45

    empty_cache = LRUCache(0)
    empty_cache.put(1, 10)
    assert empty_cache.get(1) == -1

    print("LRU Cache tests passed.")
    
if __name__ == "__main__":
    test_lru_cache()