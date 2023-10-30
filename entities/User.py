class User:
    def __init__(self, userId, name):
        self.userId = userId
        self.name = name

    def __str__(self):
        return f'{self.userId} {self.name}'

    def __repr__(self):
        return f'{self.userId} {self.name}'

    def __eq__(self, other):
        return self.userId == other.userId

    def __hash__(self):
        return hash(self.userId)

    def __lt__(self, other):
        return self.userId < other.userId

    def __gt__(self, other):
        return self.userId > other.userId

    def __le__(self, other):
        return self.userId <= other.userId

    def __ge__(self, other):
        return self.userId >= other.userId
