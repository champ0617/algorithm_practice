import random


class RandomizedSet:
    def __init__(self):
        self.container = set()

    def insert(self, val: int) -> bool:
        if self.container.__contains__(val):
            return False
        self.container.add(val)
        return True

    def remove(self, val: int) -> bool:
        if self.container.__contains__(val):
            self.container.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.container))


if __name__ == "__main__":
    randomizedSet = RandomizedSet()
    print(randomizedSet.insert(1))
    print(randomizedSet.remove(2))
    print(randomizedSet.insert(2))
    print(randomizedSet.getRandom())
    print(randomizedSet.remove(1))
    print(randomizedSet.insert(2))
    print(randomizedSet.getRandom())