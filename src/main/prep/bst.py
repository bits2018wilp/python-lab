from src.main.prep.counter import Counter

class Node:

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def __eq__(self, other):
        return other != None and self.value == other.value
               #and self.left == other.left and self.right == other.right

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def set_value(self, val):
        self.value = val

class BST:

    def __init__(self, node):
        self.root = node


    def __add(self,node, root):

        if root is None:
            return

        if node.value < root.value:
            if root.left is None:
                root.left = node
                return
            else:
                self.__add(node, root.left)
        else:
            if root.right is None:
                root.right = node
                return
            else:
                self.__add(node, root.right)

    def add(self, node):
        self.__add(node, self.root)



    def inorder(self, node, list):

        if node is None:
            return

        self.inorder(node.left, list)
        list.append(node.value)
        self.inorder(node.right, list)

    def postorder(self, node, list):

        if node is None:
            return

        self.inorder(node.left, list)
        self.inorder(node.right, list)
        list.append(node.value)

    def preorder(self, node, list):

        if node is None:
            return

        list.append(node.value)
        self.inorder(node.left, list)
        self.inorder(node.right, list)

    def findmin(self, root):

        while root and root.left:
            root = root.left
        return root


    def inorder_successor(self, root, node, found, key):

        if root is None:
            return

        if root.value == key:
            found.append(True)
            m = self.findmin(root.right)
            if m is not None:
                node.clear()
                node.append(m)

        elif key < root.value:
            node.clear()
            node.append(root)
            self.inorder_successor(root.left, node, found, key)

        else:
            self.inorder_successor(root.right, node, found, key)


    def findmax(self, root):

        while root and root.left:
            root = root.left
        return root

    def find_sl(self, root, l, sl):

        if root is None:
            return

        if root.value > l.value:
            sl.set_value(l.value)
            l.set_value(root.value)

        self.find_sl(root.left, l, sl)
        self.find_sl(root.right, l, sl)

    def find_second_largest(self, root, l, sl):

        if not root:
            return

        if root.right:
            self.find_sl(root.right, l, sl)
        else:
            tmp = root
            self.find_sl(root.left, l, sl)
        print(l, sl)

    def find_sl2(self, root, counter):

        if root is None or counter.get_count() >= 2:
            return


        self.find_sl2(root.right, counter)

        counter.increment()
        if counter.get_count() == 2:
            print(root)
            return

        self.find_sl2(root.left, counter)

    def inorder_predecessor(self, root, node, found, key):

        if root is None:
            return

        if root.value == key:
            print('abt to get')
            found.append(True)
            m = self.findmax(root.left)
            if m is not None:
                node.clear()
                node.append(m)

        elif key < root.value:
            # node.clear()
            # node.append(root)
            self.inorder_successor(root.left, node, found, key)

        else:
            node.clear()
            node.append(root)
            self.inorder_successor(root.right, node, found, key)


if __name__ == '__main__':

    root = Node(15)

    bst = BST(root)
    bst.add(Node(13))
    bst.add(Node(11))
    bst.add(Node(9))
    bst.add(Node(7))
    bst.add(Node(50))
    bst.add(Node(60))
    bst.add(Node(70))
    bst.add(Node(45))
    bst.add(Node(35))
    bst.add(Node(48))
    bst.add(Node(14))

    list =[]
    bst.preorder(root, list)
    print(list)
    lst = [None] * 2

    # l = Node(0)
    # sl = Node(0)
    # bst.find_second_largest(root, l, sl)
    # print(l, sl)

    counter = Counter(0)
    bst.find_sl2(root, counter)
    print(counter)
    # succ = []
    # found = []
    # bst.inorder_successor(root, succ, found, 13)
    # if True in found:
    #     print(succ)
    #
    # found = []
    # succ =[]
    # bst.inorder_predecessor(root, succ, found, 14)
    # if True in found:
    #     print(succ)
    #
