#!/usr/local/bin/python3

class Node:
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.next = None


class LinkedList:
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
            self.size += 1
            return
        else:
            self.tail.next = newNode
            self.tail = newNode
            return
    
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
