'''
An XOR linked list is a more memory efficient doubly linked list.
 Instead of each node holding next and prev fields, it holds a field named both,
 which is an XOR of the next node and the previous node.
 Implement an XOR linked list; it has an add(element) which adds the element to the end,
 and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
'''

iclass Node(object):
    def __init__(self, val = None, both = None):
        self.val = val
        self.both = None

class XOR_List(object):
    def __init__(self, Node = None):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.length = 0

    def add(self, element):
        if length == 0:
            self.head.both = 0 ^ get_pointer(element)
            self.tail.both = get_pointer(element) ^ 0
            element.both = get_pointer(self.head) ^ get_pointer(self.tail)
        else:
            prev = dereference_pointer(self.tail.both)
            prev_prev_addr = prev.both ^ get_pointer(self.tail)
            prev.both = prev_prev_addr ^ get_pointer(element)
            element.both = get_pointer(prev) ^ get_pointer(self.tail.both)
            self.tail.both = get_pointer(element) ^ 0
        length += 1

    def get(self, index):
        if index >= length:
            raise ValueError('Invalid Index!')
        else:
            ptr = self.head.both
            prev_addr = get_pointer(self.head)

            while index > 0:
                node = dereference_pointer(ptr)
                ptr = node.both ^ prev_addr
                prev_addr = ptr
                index -= 1

            if index == 0:
                return dereference_pointer(ptr)


def main():
    pass


if __name__ == '__main__':
    main()