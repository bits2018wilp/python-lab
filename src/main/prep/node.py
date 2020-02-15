class Node:

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        self.prev = None
        self.next = None
        self.heapref = None
        self.random = None
        self.clonenode = None
        self.parent = None
        self.children = []
        self.lock = False

    def __eq__(self, other):
        return other != None and self.value == other.value # and self.left == other.left and self.right == other.right

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def set_value(self, val):
        self.value = val

    def set_heap_ref(self, heapref):
        self.heapref = heapref

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value