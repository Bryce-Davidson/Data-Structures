#! /usr/bin/python3

class Node:
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        newNode = Node(data)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        if self.size == 0:
            self.tail = newNode
        self.size += 1

    def __str__(self):
        s = "["
        curNode = self.head
        while curNode != None:
            s += str(curNode.data)
            if curNode.next:
                s += ", "
            curNode = curNode.next
        s += "]"
        return s



def print_test(truth_value, test_number):
    s = "Test {}: ".format(test_number)
    if truth_value:
        s += "PASS"
    else:
        s += "FAIL"
    print(s)

def append_test():
    lli = SinglyLinkedList()
    lli.append("Hello")
    lli.append("World!")
    print_test(lli.__str__() == "[Hello, World!]", "append")

def push_test():
    lli = SinglyLinkedList()
    lli.push("Hello")
    lli.push("World!")
    lli.push("Why?")
    print_test(lli.__str__() == "[Why?, World!, Hello]", "push")

def push_append_test():
    lli = SinglyLinkedList()
    lli.push(1)
    lli.append(2)
    lli.push(0)
    lli.append(3)
    print_test(lli.__str__() == "[0, 1, 2, 3]", "push_append")
    return

def main():
    append_test()
    push_test()
    push_append_test()

if __name__ == '__main__':
    main()