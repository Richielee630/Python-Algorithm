import time
import random


class Array_Search:
    def __init__(self, array):
        self.array = array

    def init_array_search(self, val_array):
        self.array = Array_Search(val_array)

    def squential_search(self, key):

        idx = 0
        for num in self.array:
            if num == key:
                return idx
            idx = idx + 1
        return False

    def bsearch(self, val):

        l, e = 0, len(self.array) - 1
        while l + 1 < e:
            m = l + ((e - l) >> 1)
            if val < self.array[m]:
                e = m
            else:
                l = m

        if self.array[l] == val:
            return True
        if self.array[e] == val:
            return True
        return False


class BST_Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def init_bst(self, val):
        self.root = BST_Node(val)

    def insert(self, val):
        if self.root is None:
            self.init_bst(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, current, val):

        p, cur = None, self.root
        while cur is not None:
            p = cur
            if cur.val == val:
                break
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        if cur is not None:
            return False

        if val < p.val:
            p.left = BST_Node(val)
        else:
            p.right = BST_Node(val)

        return True

    def bsearch(self, val):

        cur = self.root
        while cur is not None:
            if cur.val == val:
                return True

            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        return False

    def searchNode(self, current, val):
        # return parent node

        p, cur = None, self.root
        while cur is not None:
            if cur.val == val:
                break

            p = cur
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.lright

        return p

    def delete(self, val):
        if self.root is None:
            return False

        tp, t = self.searchNode(self.root, val), None
        if tp is None:
            t = self.root
        else:
            if val < tp.val:
                t = tp.left
            else:
                t = tp.right

        if t is None:
            return False

        if t.left is not None and t.right is not None:
            cp, c = t, t.right
            while c.left is not None:
                cp, c = c, c.left

            t.val = c.val
            tp, t = cp, c

        c = None
        if t.left is not None:
            c = t.left
        if t.right is not None:
            c = t.right

        if tp is None:
            self.root = c
        else:
            if t == tp.left:
                tp.left = c
            else:
                tp.right = c

        return True


class RBBST_Node:
    def __init__(self, val, color):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.color = color


RED = True
BLACK = False


class RBBST:
    def __init__(self):
        self.root = None

    def init_rbbst(self, val, color):
        self.root = RBBST_Node(val, color)

    def is_red(self, current):
        return current.color

    def rotate_left(self, current):

        p = current.parent
        r = current.right
        current.right = r.left
        if r.left is not None:
            r.left.parent = current
        r.left = current
        current.parent = r

        if p is None:
            self.root = r
        else:
            if current == p.left:
                p.left = r
            else:
                p.right = r
            r.parent = p
        return r

    def rotate_right(self, current):

        p = current.parent
        l = current.left
        current.left = l.right
        if l.right is not None:
            l.right.parent = current
        l.right = current
        current.parent = l

        if p is None:
            self.root = l
        else:
            if current == p.left:
                p.left = l
            else:
                p.right = l
            l.parent = p
        return l

    def flip_colors(self, current):
        current.color = ~current.color
        return True

    def insert(self, val):
        if (self.root is None):
            self.init_rbbst(val, RED)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, current, val):

        p, cur = None, self.root
        while cur is not None:
            p = cur
            if cur.val == val:
                break
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        if cur is not None:
            return False

        if val < p.val:
            p.left = BST_Node(val)
        else:
            p.right = BST_Node(val)

        return True

    def bsearch(self, val):

        cur = self.root
        while cur is not None:
            if cur.val == val:
                return True

            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        return False

    def searchNode(self, current, val):
        # return parent node

        cur = self.root
        while cur is not None:
            if cur.val == val:
                break

            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        return cur


if __name__ == "__main__":

    set_sz = 10
    tut = BST()

    vals = random.sample(range(1, 100), set_sz)
    print(vals)
    for idx in range(set_sz - 1):
        tut.insert(vals[idx])

    print(tut.bsearch(vals[1]))
    print(tut.bsearch(11))

    tut_rb = RBBST()

    for idx in range(set_sz - 1):
        tut_rb.insert(vals[idx])

    print(tut.bsearch(vals[1]))
    print(tut.bsearch(11))
