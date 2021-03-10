from Lists.linked_list.singly_linked_list import SinglyLinkedList, Node
import unittest

class TestSingly(unittest.TestCase):

    def test_to_list(self):
        sll = SinglyLinkedList()
        sll.append(1)
        sll.append(2)
        sll.append(3)
        self.assertListEqual(sll.to_list(), [1,2,3])

    # (1) a constructor for creating an empty list
    def test_constructor(self):
        sll = SinglyLinkedList()
        self.assertIsInstance(sll, SinglyLinkedList)

    # (2) an operation for testing whether or not a list is empty
    def test_is_empty(self):
        sll = SinglyLinkedList()
        self.assertTrue(sll.is_empty())

    # (3) an operation for prepending an entity to a list
    def test_prepend(self):
        sll = SinglyLinkedList()
        sll.push(1)
        sll.push(2)
        sll.push(3)
        self.assertListEqual(sll.to_list(), [3,2,1])

    # (4) an operation for appending an entity to a list
    def test_append(self):
        sll = SinglyLinkedList()
        sll.append(1)
        sll.append(2)
        sll.append(3)
        self.assertListEqual(sll.to_list(), [1,2,3])

    # (5) an operation for determining the
    #  first component (or the 'head') of a list
    def test_get_head(self):
        sll = SinglyLinkedList()
        head = sll.head
        self.assertIs(sll.head, head)

    # (6) an operation for referring to the list consisting
    # of all the components of a list except for its first
    # (this is called the 'tail' of the list.)
    def test_get_tail(self):
        sll = SinglyLinkedList()
        sll.append(1)
        tail = sll.get_tail()
        self.assertIs(sll.head.next, tail)

        # Empty list
        with self.assertRaises(IndexError):
            sll = SinglyLinkedList()
            sll.get_tail()

    # (7) an operation for accessing the element at a given index
    def test_get_by_index(self):
        sll = SinglyLinkedList()
        sll.append(1)
        sll.append(2)
        value = sll[1]
        self.assertEqual(value, 2)

        # Empty list error
        with self.assertRaises(IndexError):
            value = sll[10]

        # Index out of bounds error
        with self.assertRaises(IndexError):
            sll = SinglyLinkedList()
            value = sll[1]

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

    def test_find_by_value(self):
        sll = SinglyLinkedList()

        # Empty list test
        with self.assertRaises(KeyError):
            sll.find_by_value("foo")

        sll.append("Bar")
        sll.append("James")
        sll.append("Foo")
        james = sll[1]
        result = sll.find_by_value("James")
        self.assertIs(james, result)

        # Cannot find value test
        with self.assertRaises(KeyError):
            result = sll.find_by_value("not in list")

    def test_pop_left(self):
        sll = SinglyLinkedList()
        sll.append(1)
        sll.append(2)
        node = sll.pop_left()
        self.assertIsInstance(node, Node)
        self.assertEqual(node.data, 1)
        self.assertListEqual(sll.to_list(), [2])

    def test_pop(self):
        sll = SinglyLinkedList()
        sll.append(1)
        sll.append(2)
        node = sll.pop()
        self.assertIsInstance(node, Node)
        self.assertEqual(node.data, 2)
        self.assertListEqual(sll.to_list(), [1])

    def test_remove_at_index(self):
        sll = SinglyLinkedList()

        with self.assertRaises(IndexError):
            # Delete on empty list
            del sll[0]
            # Delete index out of bounds
            del sll[10]

        sll.append(0)
        sll.append(1)
        sll.append(2)
        sll.append(3)

        # Delete middle node
        del sll[2]
        self.assertListEqual(sll.to_list(), [0,1,3])

        # Delete tail node
        del sll[2]
        self.assertListEqual(sll.to_list(), [0,1])

        # Delete first node
        del sll[0]
        self.assertListEqual(sll.to_list(), [1])



if __name__ == "__main__":
    unittest.main()