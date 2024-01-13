class RedBlackNode:
    def __init__(self, val=0):
        self.val = val
        self.red = False
        self.right = None
        self.left = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.leaf = RedBlackNode()
        self.root = self.leaf

    def insert(self, val):
        nn = RedBlackNode(val)
        nn.red = True

        nn.left = self.leaf
        nn.right = self.leaf

        parent = None
        cn = self.root

        while cn != self.leaf:
            parent = cn
            if nn.val < cn.val:
                cn = cn.left
            elif nn.val > cn.val:
                cn = cn.right
            else:
                return

        nn.parent = parent
        if parent is None:
            self.root = nn
        elif nn.val < parent.val:
            parent.left = nn.val
        else:
            parent.right = nn.val

        self.fix_insert()


