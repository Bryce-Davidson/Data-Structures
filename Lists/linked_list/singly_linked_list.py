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

    "O(n)"
    def to_list(self):
        li = []
        if self.is_empty():
            raise IndexError("Cannot convert empty list to list.")
            
        curNode = self.head
        while curNode:
            li.append(curNode.data)
            curNode = curNode.next
        return li

    "O(1)"
    def append(self, data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        self.tail = newNode
    
    def push(self, data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
            return
        newNode.next = self.head
        self.head = newNode

    def get_tail(self):
        if self.is_empty():
            raise IndexError("Empty list")
        return self.head.next

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop empty list.")
        curNode = self.head
        if curNode == self.tail:
            self.head = None
            self.tail = None
            return
        while curNode:
            if curNode.next == self.tail:
                curNode.next = None
                return
            curNode = curNode.next
    
    def pop_left(self):
        if self.is_empty():
            raise IndexError("Cannot pop_left empty list.")
        self.head = self.head.next

    def find_by_value(self, value):
        if self.is_empty():
            raise KeyError(f'Cannot key empty list.')
        curNode = self.head
        while curNode:
            if curNode.data == value:
                return curNode.data
            curNode = curNode.next
        raise KeyError("Cannot find {value} in list.")

    def __getitem__(self, i):  
        if self.is_empty():
            raise IndexError(f'Cannot index empty list.')
        curNode = self.head
        idx = 0
        while curNode:
            if idx == i:
                return curNode.data
            curNode = curNode.next
            idx += 1
        raise IndexError("Index is out of bounds.")

    def __setitem__(self, i, value):
        if self.is_empty():
            raise IndexError(f'Cannot set item for empty list.')
        curNode = self.head
        idx = 0
        while curNode:
            if idx == i:
                curNode.data = value
                return
            curNode = curNode.next
            idx += 1
        raise IndexError("Index is out of bounds.")
        
    def __delitem__(self, i):
        # empty
        if self.is_empty():
            raise IndexError(f'Cannot delete item for empty list.')
        # one item
        if self.head == self.tail:
            self.head == None
            self.tail == None
        # more than one item
        idx = 0
        curNode = self.head
        while curNode:
            # if the next node is to be deleted
            if idx+1 == i:
                # if the node to be deleted is the tail
                if curNode.next == self.tail:
                    curNode.next = None
                    self.tail = curNode
                    return
                # if in middle
                curNode.next = curNode.next.next
                return
            curNode = curNode.next
            idx += 1
        raise IndexError("Index is out of bounds.")

    def __str__(self):
        s = "["
        curNode = self.head
        while curNode:
            s += str(curNode.data)
            if curNode.next:
                s += ", "
            curNode = curNode.next
        s += "]"
        return s

def remove_at_index_test():
    sll = SinglyLinkedList()
    sll.append(0)
    sll.append(1)
    sll.append(2)
    sll.append(3)
    del sll[2]
    print_test(str(sll) == "[0, 1, 3]", "RAI - middle")
    del sll[2]
    print_test(str(sll) == "[0, 1]", "RAI - tail")
    del sll[1]
    print_test(str(sll) == "[0]", "RAI - head")

def remove_by_value_test():
    return

def reversal_of_list_test():
    return

def main():
    constructor_test()
    is_empty_test()
    prepend_test()
    append_test()
    get_head_test()
    get_tail_test()
    get_by_index_test()
    
    set_by_index_test()
    find_by_value_test()

    remove_at_beggining_test()
    remove_at_end_test()
    remove_at_index_test()
    remove_by_value_test()

    reversal_of_list_test()

    return

if __name__ == '__main__':
    main()