# -*- coding: utf-8 -*-
# @Date    : 2022-07-25 09:10:55
# @Author  : DENCODER (hetcjoshi1684@gmail.com)
# @GitHub    : (https://github.com/D-ENCODER)
# @Twitter    : (https://twitter.com/Hetjoshi1684)
# @Version : 1.0.0

class newNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def isBST(root, l=None, r=None):
    if (root == None):
        return True
    if (l != None and root.data <= l.data):
        return False
    if (r != None and root.data >= r.data):
        return False
    return isBST(root.left, l, root) and \
        isBST(root.right, root, r)


if __name__ == '__main__':
    root = newNode(3)
    root.left = newNode(2)
    root.right = newNode(5)
    root.right.left = newNode(1)
    root.right.right = newNode(4)
    root.right.left.left = newNode(40)
    if (isBST(root, None, None)):
        print("Is BST")
    else:
        print("Not a BST")
