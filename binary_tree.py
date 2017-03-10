

class Node(object):

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree(object):

    def __init__(self):
        self.root = Node()

    def lookup(self, node=None, data=None):
        if node is None:
            raise ValueError("Data is not found.")

        if data < node.data:
            return self.lookup(node=node.left, data=data)
        elif data > node.data:
            return self.lookup(node=node.right, data=data)
        else:
            return True
