

class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def lookup(self, node=None, data=None):
        if node is None:
            raise ValueError("Data is not found.")

        if data < node.data:
            return self.lookup(node=node.left, data=data)
        elif data > node.data:
            return self.lookup(node=node.right, data=data)
        else:
            return True

    def insert(self, node=None, data=None):
        if node is None:
            return Node(data=data)

        if data <= node.data:
            node.left = self.insert(node=node.left, data=data)
        else:
            node.right = self.insert(node=node.right, data=data)

        return node

    def min(self, node=None):
        if node is None:
            return None

        if node.left is None:
            return node
        else:
            return self.min(node=node.left)

    def max(self, node=None):
        if node is None:
            return None

        if node.right is None:
            return node
        else:
            return self.max(node=node.right)
