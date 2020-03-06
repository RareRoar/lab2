class Vector:

    def get_size(self):
        return len(self.components)

    size = property(get_size)

    def __init__(self, *components):
        self.components = []
        components = list(components)
        if isinstance(components[0], list):
            components = components[0]
        for item in components:
            if isinstance(item, int) or isinstance(item, float):
                self.components.append(item)

    def __str__(self):
        return '[' + ' '.join([str(i) for i in self.components]) + ']'

    def __add__(self, other):
        if self.size == other.size:
            temp = [0] * self.size
            for i in range(self.size):
                temp[i] = self.components[i] + other.components[i]
            return Vector(temp)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector([other * item for item in self.components])
        else:
            raise ValueError("'Vector' object can be only multiplied by a number")

    def __sub__(self, other):
        return self + other * -1

    def __eq__(self, other):
        temp = self.components[0] / other.components[0]
        for i in range(1, self.size):
            if temp != self.components[0] / other.components[0]:
                return False
        return True

    def scalar(self, other):
        result = 0
        for i in range(self.size):
            result += self.components[i] * other.components[i]
        return result

    def __getitem__(self, item):
        return self.components[item]

    def norm(self):
        result = 0
        for i in range(self.size):
            result += self.components[i] * 2
        return result
