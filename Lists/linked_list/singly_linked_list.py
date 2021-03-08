#! /usr/bin/python3
class Node:
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return not self.head and not self.tail

    def to_list(self):
        li = []
        cur_node = self.head
        while cur_node:
            li.append(cur_node.data)
            cur_node = cur_node.next
        return li

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def get_tail(self):
        if self.is_empty():
            raise IndexError("Empty list")
        return self.head.next

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop empty list.")
        cur_node = self.head
        if cur_node == self.tail:
            self.head = None
            self.tail = None
            return
        while cur_node:
            if cur_node.next == self.tail:
                cur_node.next = None
                return
        cur_node = cur_node.next

    def pop_left(self):
        if self.is_empty():
            raise IndexError("Cannot pop_left empty list.")
        self.head = self.head.next

    def find_by_value(self, value):
        if self.is_empty():
            raise KeyError("Empty list.")
        cur_node = self.head
        while cur_node:
            if cur_node.data == value:
                return cur_node.data
            cur_node = cur_node.next
        raise KeyError("Cannot find {value} in list.")

    def __getitem__(self, i):  
        if self.is_empty():
            raise IndexError("Cannot index empty list.")
        cur_node = self.head
        idx = 0
        while cur_node:
            if idx == i:
                return cur_node.data
            cur_node = cur_node.next
            idx += 1
        raise IndexError("Index is out of bounds.")

    def __setitem__(self, i, value):
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
        # empty
        if self.is_empty():
            raise IndexError("Cannot delete item for empty list.")
        # one item
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # more than one item
        idx = 0
        cur_node = self.head
        while cur_node:
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
