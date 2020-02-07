class Counter:

    def __init__(self, val):
        self.count = val

    def increment(self):
        self.count +=1
        return self

    def get_count(self):
        return self.count

    def set_count(self, value):
        self.count = value

    def add(self, val):
        self.count += val
        return self

    def __str__(self):
        return str(self.count)
    def __repr__(self):
        return str(self.count)

class Boolean:

    def __init__(self):
        self.value = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def OR(self, val):
        self.value = self.value or val
        return self

    def AND(self, val):
        self.value = self.value and val
        return self

    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return str(self.value)

class Object:

    def __init__(self):
        self.value = None

    def set(self, val):
        self.value = val

    def get(self):
        return self.value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)
