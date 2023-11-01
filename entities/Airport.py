class Airport:
    def __init__(self, code, name, city, state):
        self.code = code
        self.name = name
        self.city = city
        self.state = state

    def __str__(self):
        return f'{self.code} {self.name} {self.city} {self.state}'

    def __repr__(self):
        return f'{self.code} {self.name} {self.city} {self.state}'

    def __eq__(self, other):
        return self.code == other.code

    def __hash__(self):
        return hash(self.code)

    def __lt__(self, other):
        return self.code < other.code

    def __gt__(self, other):
        return self.code > other.code

    def __le__(self, other):
        return self.code <= other.code

    def __ge__(self, other):
        return self.code >= other.code

    def __ne__(self, other):
        return self.code != other.code

    def __contains__(self, item):
        return item in self.code

    def __len__(self):
        return len(self.code)

    def get_code(self):
        return self.code

    def get_name(self):
        return self.name

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def set_code(self, code):
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state
