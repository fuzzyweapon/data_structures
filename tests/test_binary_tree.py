import pytest
from binary_tree import Node, BinaryTree

class TestNode:
    def test_structure(self):
        node = Node(data='one')
        second_node = Node(data='two')
        third_node = Node(data='three',left=node, right=second_node)
        assert third_node.data == 'three'
        assert third_node.left.data == 'one'
        assert third_node.right.data == 'two'

class TestBinaryTree:

    def setup_method(self):
        self.binary_tree = BinaryTree()

    def test_lookup(self):
        self.binary_tree.root.data = 'two'
        self.binary_tree.root.left = Node(data='one')
        self.binary_tree.root.right = Node(data='tww')

        assert self.binary_tree.lookup(self.binary_tree.root, data='one') is True
        assert self.binary_tree.lookup(self.binary_tree.root, data='two') is True
        assert self.binary_tree.lookup(self.binary_tree.root, data='tww') is True

    def test_lookup_not_found(self):
        with pytest.raises(ValueError):
            self.binary_tree.lookup(self.binary_tree.root, data='foo')
