
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data=None):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def size(self):
        current_node = self.head
        count = 0

        while current_node:
            count += 1
            current_node = current_node.next_node
        return count

    def search(self, data=None):
        current_node = self.head
        found = False

        while current_node and found is False:
            if current_node.data == data:
                found = True
            else:
                current_node = current_node.next_node

        if found is not True:
            raise ValueError("Data was not found in the list.")

        return current_node

    def delete(self, data=None):
        current_node = self.head
        previous_node = None
        found = False

        while current_node and found is False:
            if current_node.data == data:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.next_node

        if found is True:
            next_node = current_node.next_node

            if previous_node is None:
                self.head = next_node
            else:
                previous_node.next_node = next_node
        else:
            raise ValueError("Data was not found in the list.")
