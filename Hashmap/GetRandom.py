import random


class RandomizedSet:

    def __init__(self):
        self.numSet = set()
        self.numList = []

    def insert(self, val: int) -> bool:
        if val in self.numSet:
            return False
        self.numSet.add(val)
        self.numList.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numSet:
            return False
        found = 0
        # find index in list
        for i in range(len(self.numList)):
            if self.numList[i] == val:
                found = i
                break

        # swap removed value with last element in list
        self.numList[found] = self.numList[len(self.numList) - 1]

        # pop last element to remove it from list and remove from set
        self.numList.pop()
        self.numSet.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.numList)
