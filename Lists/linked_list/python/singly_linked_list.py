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

    def find_by_value(self, value):
        if self.is_empty():
            raise KeyError(f'Cannot key empty list.')
        curNode = self.head
        while curNode:
            if curNode.data == value:
                return curNode.data
            curNode = curNode.next
        raise KeyError("Cannot find {value} in list.")

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
            idx += 1
            # if the next node is to be deleted
            if idx == i:
                # if the node to be deleted is the tail
                if curNode.next == self.tail:
                    curNode.next = None
                    self.tail = curNode
                    return
                # if in middle
                curNode.next = curNode.next.next
                return
            curNode = curNode.next
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

# Tests
# ---------------------------------------------------------------------------

def print_test(truth_value, test_description):
    s = "Test [{:^25}]: ".format(test_description)
    if truth_value:
        s += "PASS"
    else:
        s += "FAIL"
    print(s)

def print_ERR_test(truth_value, test_description):
    s = "\t {:>22}]: ".format(test_description)
    if truth_value:
        s += "PASS"
    else:
        s += "FAIL"
    print(s)

def constructor_test():
    sll = SinglyLinkedList()
    print_test(isinstance(sll, SinglyLinkedList), "constructor")
    return

def is_empty_test():
    sll = SinglyLinkedList()
    print_test(sll.is_empty(), "is empty")
    return

def prepend_test():
    sll = SinglyLinkedList()
    sll.push(1)
    sll.push(2)
    sll.push(3)
    print_test(sll.__str__() == "[3, 2, 1]", "prepend")
    return

def append_test():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    print_test(sll.__str__() == "[1, 2, 3]", "append")
    return

def get_head_test():
    sll = SinglyLinkedList()
    head = sll.head
    print_test(sll.head == head, "get head")

def get_tail_test():
    sll = SinglyLinkedList()
    sll.append(1)
    tail = sll.get_tail()
    print_test(sll.head.next == tail, "get tail")

def get_by_index_test():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    value = sll[1]
    print_test(value == 2, "get by index")
    try:
        value = sll[10]
    except IndexError:
        print_ERR_test(True, "IndexError")
        return
    print_ERR_test(False, "IndexError")


def set_by_index_test():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll[1] = 42
    print_test(sll[1] == 42, "set by index")

def find_by_value_test():
    sll = SinglyLinkedList()
    sll.append("Bar")
    sll.append("James")
    james = sll[1]
    sll.append("Foo")
    result = sll.find_by_value("James")
    print_test(james is result, "find by value")
    return

def remove_at_beggining_test():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.pop_left()
    print_test(str(sll) == "[2]", "pop left")

def remove_at_end_test():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.pop()
    print_test(str(sll) == "[1]", "pop")

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