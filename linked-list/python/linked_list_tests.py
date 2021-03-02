#! /usr/bin/python3
from linked_list import LinkedList, Node

def print_test(truth_value, test_number):
    s = "Test {} ".format(test_number)
    if truth_value:
        s += "PASS"
    else:
        s += "FAIL"
    print(s)

def test1():
    lli = LinkedList()
    lli.append("Hello")
    lli.append("World!")
    print_test(lli.__str__() == "[Hello, World!]", 1)

def main():
    test1()

if __name__ == '__main__':
    main()