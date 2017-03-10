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
        root = Node(data='two')
        root.left = Node(data='one')
        root.right = Node(data='tww')

        assert self.binary_tree.lookup(node=root, data='one') is True
        assert self.binary_tree.lookup(node=root, data='two') is True
        assert self.binary_tree.lookup(node=root, data='tww') is True

    def test_lookup_not_found(self):
        with pytest.raises(ValueError):
            self.binary_tree.lookup(node=self.binary_tree.root, data='foo')

    def test_insert(self):
        root = self.binary_tree.root
        root = self.binary_tree.insert(node=root, data='foo')
        assert root.data == 'foo'

    def test_insert_multiple(self):
        root = self.binary_tree.root
        root = self.binary_tree.insert(node=root, data='b')
        root = self.binary_tree.insert(node=root, data='a')
        root = self.binary_tree.insert(node=root, data='c')

        assert root.data == 'b'
        assert root.left.data == 'a'
        assert root.right.data == 'c'

    def test_min_root(self):
        root = Node(data=1)

        assert self.binary_tree.min(node=root).data == 1

    def test_min_left(self):
        root = Node(data='b')
        root.left = Node(data='a')

        assert self.binary_tree.min(node=root).data == 'a'

    def test_min_empty(self):
        assert self.binary_tree.min(node=self.binary_tree.root) is None

    def test_max_root(self):
        root = Node(data='a')
        
        assert self.binary_tree.max(node=root).data == 'a'

    def test_max_right(self):
        root = Node(data='c')
        root.right = Node(data='d')

        assert self.binary_tree.max(node=root).data == 'd'

    def test_max_empty(self):
        assert self.binary_tree.max(node=self.binary_tree.root) is None

    def test_delete_root(self):
        root = Node(data='one')
        root = self.binary_tree.delete(node=root, data='one')
        assert root is None

    def test_delete_with_left(self):
        root = Node(data=3)
        root.left = Node(data=2)
        root.left.left = Node(data=1)

        root = self.binary_tree.delete(node=root, data=2)
        assert root.left.data == 1

    def test_delete_with_right(self):
        root = Node(data=3)
        root.left = Node(data=1)
        root.left.right = Node(data=2)

        root = self.binary_tree.delete(node=root, data=1)
        assert root.left.data == 2

    def test_delete_with_both_children(self):
        root = Node(data=4)
        root.left = Node(data=2)
        root.left.left = Node(data=1)
        root.left.right = Node(data=3)

        root = self.binary_tree.delete(node=root, data=2)
        assert root.left.data == 3
        assert root.left.left.data == 1

    def test_delete_not_found(self):
        with pytest.raises(ValueError):
            self.binary_tree.delete(node=self.binary_tree.root, data=1)

    def test_size_some(self):
        root = Node(data=4)
        root.left = Node(data=2)

        assert self.binary_tree.size(node=root) == 2

    def test_size_empty(self):
        assert self.binary_tree.size(node=self.binary_tree.root) == 0

    def test_floor_one(self):
        root = Node(data='one')
        assert self.binary_tree.floor(node=root, data='one').data == 'one'

    def test_floor_with_max_child(self):
        root = Node(data=3)
        root.left = Node(data=1)
        root.left.right = Node(data=2)

        assert self.binary_tree.floor(node=root, data=3).data == 2

    def test_floor_without_max_child(self):
        root = Node(data=3)
        root.left = Node(data=1)

        assert self.binary_tree.floor(node=root, data=3).data == 1

    def test_floor_not_found(self):
        with pytest.raises(ValueError):
            self.binary_tree.floor(node=self.binary_tree.root, data='one')

    def test_ceiling_one(self):
        root = Node(data='one')
        assert self.binary_tree.ceiling(node=root, data='one').data == 'one'

    def test_ceiling_with_min_child(self):
        root = Node(data=1)
        root.right = Node(data=3)
        root.right.left = Node(data=2)

        assert self.binary_tree.ceiling(node=root, data=1).data == 2

    def test_ceiling_without_min_child(self):
        root = Node(data=1)
        root.right = Node(data=3)

        assert self.binary_tree.ceiling(node=root, data=1).data == 3

    def test_ceiling_not_found(self):
        with pytest.raises(ValueError):
            self.binary_tree.ceiling(node=self.binary_tree.root, data='one')
