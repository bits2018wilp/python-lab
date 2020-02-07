import math

class Stackk:

    def __init__(self, k):
        self.k = k
        self.stack = []
        print('stack of size: ', k)

    def push(self, val):

        if len(self.stack) == self.k:
            return False
        else:
            self.stack.append(val)
            return True

    def pop(self):
        if len(self.stack) == 0:
            return False
        else:
            p = self.stack.pop()
            return p

    def __repr__(self):
        return str(self.stack)

class SOS:

    def __init__(self, k, n):

        self.k = k
        self.n = n

        self.nos = math.ceil(n/k)
        self.map = {}
        for i in range(self.nos):
            if i == self.nos-1:
                self.map[i] = Stackk(n - (k * (self.nos-1)))
            else:
                self.map[i] = Stackk(k)

        self.snumber = 0
        self.total = 0
        self.cindex = 0

        print(self.nos)

    def push(self, val):

        if self.total >= self.n:
            raise Exception('stack is full')

        stack = self.map[self.snumber]
        res = stack.push(val)
        if not res:
            if self.snumber == self.nos-1:
                raise Exception('stack full')
            else:
                self.snumber+=1
                stack = self.map[self.snumber]
                stack.push(val)

    def pop(self):

        stack = self.map[self.snumber]
        res = stack.pop()
        if not res:
            if self.snumber-1 < 0:
                raise Exception('stack empty')
            else:
                self.snumber-=1
                stack = self.map[self.snumber]
                res = stack.pop()
                return res
        else:
            return res


    def pop_at_nos(self, i):

        if i in self.map.keys():
            stack = self.map[i]
            res = stack.pop()
            if not res:
                raise Exception('stack empty')
            else:
                return res
        else:
            raise Exception('invalid stack number ', i)

    def print_stack(self):
        print(self.map)

stack = SOS(3, 7)
stack.push(1)
print(stack.pop())
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
print(stack.pop())
stack.push(11)
stack.push(12)
stack.print_stack()
stack.push(23)
stack.push(55)
stack.print_stack()
