

class Node:

    def __init__(self, val):
        self.value = val
        self. next = None


class LinkList:

    def __init__(self):
        self.start = Node(1)
        self.start.next = None
        self.current = self.start

    def add(self, value):

        tmp = Node(value)

        self.current.next = tmp
        self.current = tmp

    def rev(self):

        list = []
        tmp = self.start

        while tmp != None:
            list.append(tmp.value)
            tmp = tmp.next

        print(list)
        i = self.start
        while i != None:
            i.value = list.pop()
            i = i.next

    def rev_in_grp(self, k):

        list = []
        tmp = self.start
        s = tmp
        c = 0
        while tmp != None:
            list.append(tmp.value)
            tmp = tmp.next

            if c == k or tmp == None:
                i = s
                while c >= 0:
                    i.value = list.pop()
                    i = i.next
                    c -=1
                s = tmp
            c+=1

    def print(self):

        tmp = self.start

        while tmp != None:

            print(tmp.value)
            tmp = tmp.next


if __name__ == "__main__":

    ll = LinkList()
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)

    ll.print()

    ll.rev_in_grp(2)
    ll.print()