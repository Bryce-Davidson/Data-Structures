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
        self.size = 0

    def insert(self, data):
        if(not self.head):
            self.head = Node(data)
            self.size += 1
            return
        curNode = self.head
        for i in range(self.size):
            if(not curNode.next):
                curNode.next = Node(data)
            curNode = curNode.next
        self.size +=1
    
    def __str__(self):
        s = "["
        curNode = self.head
        for i in range(self.size):
            s += str(curNode.data)
            if i != self.size-1:
                s += ","
            curNode = curNode.next
        s += "]"
        return s
