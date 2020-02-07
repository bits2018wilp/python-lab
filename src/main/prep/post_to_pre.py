
def find_index(l, ino):

    if l in ino:
        return ino.index(l)
    else:
        return -1

def printpostorder(inorder, preorder, n):
    if preorder[0] in inorder:
        root = inorder.index(preorder[0])

    if root != 0:  # left subtree exists
        printpostorder(inorder[:root],
                       preorder[1:root + 1],
                       len(inorder[:root]))

    if root != n - 1:  # right subtree exists
        printpostorder(inorder[root + 1:],
                       preorder[root + 1:],
                       len(inorder[root + 1:]))

    print
    preorder[0],

def print_pre(post, ino, lst):

    if len(ino) == 0 or len(post) == 0:
        return

    l = post[len(post)-1]
    post.remove(l)
    #print(l, post)
    if l in ino:
        index = find_index(l, ino)
    #print(index, ino[0: index])

    #print(l)
    lst.append(l)
    if index != 0:
        print_pre( post[1:index+1], ino[: index], lst )
    if index != len(ino)-1:
        print_pre( post[index+1:], ino[index + 1:], lst )


post = [7, 9, 11, 13, 14, 35, 45, 48, 50, 60, 70, 15]
       #[15, 7, 9, 11, 13, 14, 35, 45, 48, 50, 60, 70]

ino = post.copy()
ino.sort()

print('post: ',post)
print('ino:  ', ino)
lst = []
print_pre(post, ino, lst)
print(lst)

