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
        self.binary_tree.root = Node(data='two')
        root = self.binary_tree.root
        root.left = Node(data='one')
        root.right = Node(data='tww')

        assert self.binary_tree.lookup(node=root, data='one') is True
        assert self.binary_tree.lookup(node=root, data='two') is True
        assert self.binary_tree.lookup(node=root, data='tww') is True

    def test_lookup_not_found(self):
        with pytest.raises(ValueError):
            self.binary_tree.lookup(node=self.binary_tree.root, data='foo')

    def test_insert(self):
        self.binary_tree.root = self.binary_tree.insert(node=self.binary_tree.root, data='foo')
        assert self.binary_tree.root.data == 'foo'

    def test_insert_multiple(self):
        root = self.binary_tree.root
        root = self.binary_tree.insert(node=root, data='b')
        root = self.binary_tree.insert(node=root, data='a')
        root = self.binary_tree.insert(node=root, data='c')

        assert root.data == 'b'
        assert root.left.data == 'a'
        assert root.right.data == 'c'

    def test_min_root(self):
        root = self.binary_tree.root
        root = Node(data=1)

        assert self.binary_tree.min(node=root).data == 1

    def test_min_left(self):
        root = self.binary_tree.root
        root = self.binary_tree.insert(data='b')
        root = self.binary_tree.insert(data='a')

        assert self.binary_tree.min(node=root).data == 'a'

    def test_min_empty(self):
        assert self.binary_tree.min(node=self.binary_tree.root) is None
