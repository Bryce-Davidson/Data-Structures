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
        return not self.head

    def append(self, data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
            return
        curNode = self.head
        while curNode.next:
            curNode = curNode.next
        curNode.next = newNode

    def push(self, data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
            return
        newNode.next = self.head
        self.head = newNode

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



def print_test(truth_value, test_description):
    s = "Test [{}]: ".format(test_description)
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
    return

def get_head_test():
    return

def get_tail_test():
    return

def get_by_index_test():
    return


def main():
    constructor_test()
    is_empty_test()
    prepend_test()
    append_test()
    get_head_test()
    get_tail_test()
    get_by_index_test()
    return

if __name__ == '__main__':
    main()