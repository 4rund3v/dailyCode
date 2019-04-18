"""
Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.
"""


class Node():
    previous_node = None
    next_node = None
    data = None


def solution(root_node):
    prev = None
    items = []
    reversed_items = []
    node  = root_node
    while node:
        items.append(node.data)
        prev = node
        node = node.next_node
    print('Items from forawrd are : {}'.format(items))
    node = prev
    while node:
        reversed_items.append(node.data)
        node = node.previous_node
    print('Items from reverse are : {}'.format(reversed_items))
    return reversed_items == items

if __name__ == '__main__':
    # initialize the node
    doubly_linked_list = Node()
    node2 = Node()
    node3 = Node()
    node4 = Node()
    node5 = Node()
    # set the previous node
    node5.previous_node = node4
    node4.previous_node = node3
    node3.previous_node = node2
    node2.previous_node = doubly_linked_list
    # setup the next node
    node5.next_node = None
    node4.next_node = node5
    node3.next_node = node4
    node2.next_node = node3
    doubly_linked_list.next_node = node2
    # setup the data for each node
    doubly_linked_list.data  =  1
    node2.data = 4
    node3.data = 3
    node4.data = 4
    node5.data = 1
    print(solution(doubly_linked_list))
