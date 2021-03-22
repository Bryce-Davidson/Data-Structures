class Node:
    """A Node object to use in a singly linked list.

    Attributes:
        data: the data within the node
        next: the next Node object in the list
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """A singly linked list data structure.

    Attributes:
        head: a Node object representing the first element in the list
        tail: a Node object representing the last element in the list
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        """Indicates if the list is empty

        time:  O(1)
        space: O(1)

        Returns: Boolean
            A boolean representing if the list is empty
        """
        return not self.head and not self.tail

    def to_list(self):
        """Constructs a python list object out of the singly linked list

        time:  O(n)
        space: O(n)

        Returns: list
            A list representation of the singly linked list's data
        """
        li = []
        cur_node = self.head
        while cur_node:
            li.append(cur_node.data)
            cur_node = cur_node.next
        return li

    def append(self, data):
        """Appends a new piece of data onto the end of the list

        time:  O(1)
        space: O(1)
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def push(self, data):
        """Prepends a new piece of data onto the beggining of the list

        time:  O(1)
        space: O(1)
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def get_tail(self):
        """Retrieves the node representing the end of the list

        time:  O(1)
        space: O(1)

        Returns: Node
            The Node object representing the last element in the list

        Raises:
            IndexError: empty list
        """
        if self.is_empty():
            raise IndexError("Cannot get tail on Empty list")
        return self.head.next

    def pop(self):
        """Removes the last Node object in the list

        time:  O(n)
        space: O(1)

        Returns: Node
            The popped Node from the list

        Raises:
            IndexError: empty list
        """
        if self.is_empty():
            raise IndexError("Cannot pop empty list.")
        cur_node = self.head
        if cur_node == self.tail:
            self.head = None
            self.tail = None
            return
        while cur_node:
            if cur_node.next == self.tail:
                temp = self.tail
                cur_node.next = None
                return temp
        cur_node = cur_node.next


    def pop_left(self):
        """Removes the first Node object in the list

        time:  O(1)
        space: O(1)

        Returns: Node
            The popped Node from the list

        Raises:
            IndexError: empty list
        """
        if self.is_empty():
            raise IndexError("Cannot pop_left on empty list.")
        temp = self.head
        self.head = self.head.next
        temp.next = None
        return temp

    def find_by_value(self, value):
        """Finds a Node in the list by a value given

        time:  O(n)
        space: O(1)

        Returns:
            The data of the Node if the data is in the list

        Raises:
            KeyError: empty list
            KeyError: value not in list
        """
        if self.is_empty():
            raise KeyError("Cannot find value in empty list.")
        cur_node = self.head
        while cur_node:
            if cur_node.data == value:
                return cur_node.data
            cur_node = cur_node.next
        raise KeyError("Cannot find {} in list.".format(value))

    def __getitem__(self, i):
        """Finds a Node in the list on an index given

        time:  O(n)
        space: O(1)

        Returns:
            The data at the index in the list

        Raises:
            IndexError: empty list
            IndexError: index is out of bounds
        """

        if self.is_empty():
            raise IndexError("Cannot index empty list.")

        idx = 0
        cur_node = self.head
        while cur_node:
            if idx == i:
                return cur_node.data
            cur_node = cur_node.next
            idx += 1
        raise IndexError("Index is out of bounds.")

    def __setitem__(self, i, value):
        """Sets a Node's data in the list on an index given

        time:  O(n)
        space: O(1)

        Raises:
            IndexError: cannot index empty list.
            IndexError: index is out of bounds
        """
        if self.is_empty():
            raise IndexError("Cannot set item for empty list.")

        cur_node = self.head
        idx = 0
        while cur_node:
            if idx == i:
                cur_node.data = value
                return
            cur_node = cur_node.next
            idx += 1

        raise IndexError("Index is out of bounds.")

    def __delitem__(self, i):
        """Deletes a Node in the list by an index given

        time:  O(n)
        space: O(1)

        Raises:
            IndexError: empty list
            IndexError: index is out of bounds
        """
        # Empty
        if self.is_empty():
            raise IndexError("Cannot delete item on empty list.")
        # One item
        if self.head.next is None:
            self.head = None
            self.tail = None

        # More than one item

        # If first item
        # Error will not be thrown here from pop as the list is not empty
        if i == 0:
            self.head = self.head.next
            return

        cur_node = self.head
        for idx in range(i):
            # if the next node is to be deleted
            if idx+1 == i:
                # if the node to be deleted is the tail
                if cur_node.next == self.tail:
                    cur_node.next = None
                    self.tail = cur_node
                    return
                # if in middle
                cur_node.next = cur_node.next.next
                return
            cur_node = cur_node.next
            idx += 1
        raise IndexError("Index is out of bounds.")

    def __str__(self):
        s = "["
        cur_node = self.head
        while cur_node:
            s += str(cur_node.data)
            if cur_node.next:
                s += ", "
            cur_node = cur_node.next
        s += "]"
        return s
