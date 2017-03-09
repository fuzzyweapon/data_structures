import pytest
from linked_list import Node, LinkedList


class TestNode:
    def test_get_data(self):
        node = Node(data='one', next_node=None)
        assert node.get_data() == 'one'

    def test_get_next(self):
        next_node = Node(data='two', next_node=None)
        node = Node(data='one', next_node=next_node)

        assert node.get_next() == next_node

    def test_set_next(self):
        next_node = Node(data='two', next_node=None)
        node = Node(data='one', next_node=next_node)
        new_node = Node(data='three', next_node=None)

        node.set_next(new_node)
        assert node.get_next() == new_node


class TestLinkedList:
    def setup_method(self, method):
        self.linked_list = LinkedList()

    def test_insert_node(self):
        self.linked_list.insert(data='one')
        assert self.linked_list.head.get_data() == 'one'

    def test_size(self):
        assert self.linked_list.size() == 0
        self.linked_list.insert(data='one')
        assert self.linked_list.size() == 1

    def test_found_search(self):
        self.linked_list.insert(data='one')
        self.linked_list.insert(data='two')

        assert self.linked_list.search(data='two').get_data() == 'two'

    def test_not_found_search(self):
        self.linked_list.insert(data='one')
        self.linked_list.insert(data='two')
        self.linked_list.insert(data='three')

        with pytest.raises(ValueError):
            self.linked_list.search(data='four')

    def test_delete_last(self):
        self.linked_list.insert(data='one')
        self.linked_list.insert(data='two')

        self.linked_list.delete(data='two')
        assert self.linked_list.head.get_next() is None

    def test_delete_first(self):
        self.linked_list.insert(data='one')
        self.linked_list.insert(data='two')

        self.linked_list.delete(data='one')
        assert self.linked_list.head.get_data() == 'two'

    def test_delete_missing(self):
        with pytest.raises(ValueError):
            self.linked_list.delete(data='one')
