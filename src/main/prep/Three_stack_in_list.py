
class Stack:

    def __init__(self, k, n):

        self.list = [0] * n
        self.top = [None] * k
        self.next = [i+1 for i in range(n)]
        self.next[n-1] = -1
        self.next_free_location = 0

        print(self.top)
        print(self.next)

    def push(self, val, stack_number):

        current_location = self.next_free_location
        self.next_free_location = self.next[current_location]
        self.list[current_location] = val

        self.next[current_location] = self.top[stack_number]
        self.top[stack_number] = current_location

    def pop(self, stack_number):

        tos = self.top[stack_number]
        self.top[stack_number] = self.next[tos]

        self.next[tos] = self.next_free_location
        self.next_free_location = tos

        return self.list[tos]

    def printstack(self, sn):
        top_index = self.top[sn]
        while (top_index != -1):
            print(self.list[top_index])
            top_index = self.next[top_index]

s = Stack(3, 5)
s.push(1,1)
s.push(3,2)
s.push(4,0)
s.push(5,2)
