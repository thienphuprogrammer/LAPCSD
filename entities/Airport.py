class Airport:
    def __init__(self, code, name, city, state):
        self.__code = code
        self.__name = name
        self.__city = city
        self.__state = state

    def __str__(self):
        return f'{self.__code} {self.__name} {self.__city} {self.__state}'

    def __repr__(self):
        return f'{self.__code} {self.__name} {self.__city} {self.__state}'

    def __eq__(self, other):
        return self.__code == other.__code

    def __hash__(self):
        return hash(self.__code)

    def __lt__(self, other):
        return self.__code < other.__code

    def __gt__(self, other):
        return self.__code > other.__code

    def __le__(self, other):
        return self.__code <= other.__code

    def __ge__(self, other):
        return self.__code >= other.__code

    def __ne__(self, other):
        return self.__code != other.__code

    def __contains__(self, item):
        return item in self.__code

    def __len__(self):
        return len(self.__code)

    def get_code(self):
        return self.__code

    def get_name(self):
        return self.__name

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def set_code(self, code):
        self.__code = code

    def set_name(self, name):
        self.__name = name

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state
