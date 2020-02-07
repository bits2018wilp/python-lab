
class Stack:

    def __init__(self, k, n):

        self.list = [0] * n
        self.top = [None] * k
        self.next = [i+1 for i in range(n)]
        self.next[n-1] = -1

        print(self.next)

    def pop(self, stack_number):

        tos = self.top[stack_number]
        self.top[stack_number] = self.next[tos]
        self.top[tos] = None
        

    def push(self, val, stack_number):
        pass

s = Stack(3, 10)




