
class BitArray:

    def __init__(self, size):
        self.size = size
        self.count = 0
        self.ones = []
        self.zeros = []

    def set(self, i, val):

        if i < self.size:

            if val == 0:
                if i in self.ones:
                    self.ones.remove(i)
                self.zeros.append(i)
            else:
                if i in self.zeros:
                    self.zeros.remove(i)
                self.ones.append(i)
        else:
            raise IndexError

    def get(self, i):

        if i in self.ones:
            return 1
        elif i in self.zeros:
            return 0
        else:
            return

bitarray = BitArray(3)
bitarray.set(1, 0)
bitarray.set(0, 1)
bitarray.set(3, 1)

print(bitarray.get(0))
print(bitarray.get(1))
