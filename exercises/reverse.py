from node import Node
from itertools import chain

numbers = Node(1, Node(2, Node(3)))

#print(numbers)

def revers(head):
    new_head = None
    while head:
        new_head = Node(head.value, new_head)
        head = head.next
    return new_head

revers(numbers)

print(revers(numbers))