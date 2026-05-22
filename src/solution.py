class Solution:
    def __init__(self):
        self.items = []

    def add(self, value):
        if value < 0:
            raise ValueError("Value must be positive")
        self.items.append(value)

    def total(self):
        if not self.items:
            return 0
        return sum(self.items)