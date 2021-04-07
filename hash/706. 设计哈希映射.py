"""
0 <= key, value <= 106
最多调用 104 次 put、get 和 remove 方法

"""


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.data = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """

        self.data[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """

        return self.data.get(key, -1)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.data.pop(key, None)


if __name__ == "__main__":
    hash_map = MyHashMap()
    print(hash_map.put(1, 1))
    print(hash_map.put(2, 2))
    print(hash_map.get(1))
    print(hash_map.get(3))
    print(hash_map.put(2, 1))
    print(hash_map.get(2))
    print(hash_map.remove(2))
    print(hash_map.get(2))
