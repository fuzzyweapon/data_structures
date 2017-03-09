import pytest
from linked_list import Node, LinkedList


class TestLinkedList:
    def setup_method(self, method):
        self.linked_list = LinkedList()

    def test_insert_node(self):
        self.linked_list.insert(data='one')
        assert self.linked_list.head.data == 'one'

    def test_size(self):
        assert self.linked_list.size() == 0
        self.linked_list.insert(data='one')
        assert self.linked_list.size() == 1

    def test_found_search(self):
        self.linked_list.insert(data='one')
        self.linked_list.insert(data='two')

        assert self.linked_list.search(data='two').data == 'two'

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
        assert self.linked_list.head.next_node is None

    def test_delete_first(self):
        self.linked_list.insert(data='one')
        self.linked_list.insert(data='two')

        self.linked_list.delete(data='one')
        assert self.linked_list.head.data == 'two'

    def test_delete_missing(self):
        with pytest.raises(ValueError):
            self.linked_list.delete(data='one')
