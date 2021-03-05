#! /usr/bin/python3

from singly_linked_list import SinglyLinkedList
import unittest

class TestSingly(unittest.TestCase):

    def test_constructor(self):
        sll = SinglyLinkedList()
        self.assertIsInstance(sll, SinglyLinkedList)

    def test_is_empty(self):
        sll = SinglyLinkedList()
        self.assertTrue(sll.is_empty())

    def test_to_list(self):
        sll = SinglyLinkedList()
        sll.append(1)
        sll.append(2)
        sll.append(3)
        self.assertListEqual(sll.to_list(), [1,2,3])

    def test_append(self):
        sll = SinglyLinkedList()
        sll.append(1)
        sll.append(2)
        sll.append(3)
        self.assertListEqual(sll.to_list(), [1,2,3])

    def test_prepend(self):
        sll = SinglyLinkedList()
        sll.push(1)
        sll.push(2)
        sll.push(3)
        self.assertListEqual(sll.to_list(), [3,2,1])
    
    def test_get_head(self):
        sll = SinglyLinkedList()
        head = sll.head
        self.assertIs(sll.head, head)

    def test_get_tail(self):
        sll = SinglyLinkedList()
        sll.append(1)
        tail = sll.get_tail()
        self.assertIs(sll.head.next, tail)
    
    def test_get_by_index(self):
        sll = SinglyLinkedList()
        sll.append(1)
        sll.append(2)
        value = sll[1]
        self.assertEqual(value, 2)

        with self.assertRaises(IndexError):
            sll[10]
        
        with self.assertRaises(IndexError):
            sll = SinglyLinkedList()
            sll[1]

    def test_set_by_index(self):
        sll = SinglyLinkedList()
        sll.append(1)
        sll.append(2)
        sll[1] = 42
        self.assertListEqual(sll.to_list(), [1,42])
        
        with self.assertRaises(IndexError):
            sll[10] = 42
        
        with self.assertRaises(IndexError):
            sll = SinglyLinkedList()
            sll[1] = 10

if __name__ == "__main__":
    unittest.main()