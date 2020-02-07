
class Node:

    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

    def __eq__(self, other):
        return other != None and self.value == other.value and self.next == other.next and self.prev == other.prev

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __hash__(self):
        return hash(self.value)

class LRUCache:

    def __init__(self, size):

        self.start = None
        self.lmap = {}
        self.size = size
        self.current = None
        self.last = None
        self.current_size = 0

    def find(self, key):

        if key in self.lmap:
            node =  self.lmap[key]

            np = node.prev
            nn = node.next
            np.next = nn
            nn.prev = np

            self.start.prev = node
            node.next= self.start
            self.start = node
            return node
        else:
            return None

    def add(self, key):

        node = Node(key)
        if self.current_size < self.size:

            if self.start:
                self.start.prev = node
                node.next = self.start
                self.start = node
                self.current_size +=1
                self.lmap[key] = node
                return node
            else:
                self.start = node
                self.lmap[key] = node
                self.current_size +=1
                return node
        else:

            tmp = self.start
            l = None
            while tmp:
                l = tmp
                tmp = tmp.next

            self.start.prev = node
            node.next = self.start
            self.start = node
            self.current_size += 1
            self.lmap[key] = node
            print('last node: ', l, l.next, l.prev)

            del(self.lmap[l.value])
            print(self.lmap)
            l.prev.next = None
            return node

    def print_cache(self):

        print(self.lmap)

        t = self.start
        while t:
            print(t)
            t= t.next

def main():

    cache = LRUCache(4)

    cache.add(1)
    cache.add(2)
    cache.add(3)
    cache.add(4)
    cache.add(5)
    cache.print_cache()
    cache.find(3)
    cache.print_cache()

if __name__ == '__main__':

    main()