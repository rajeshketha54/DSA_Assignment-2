# Reverse a linked list in groups of given size
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_in_groups(head, k):
    current = head
    next = None
    previous = None
    count = 0

    while current is not None and count < k:
        next = current.next
        current.next = previous
        previous = current
        current = next
        count += 1

    if next is not None:
        head.next = reverse_in_groups(next, k)

    return previous

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

k = 3
reversed_head = reverse_in_groups(head, k)

current = reversed_head
while current is not None:
    print(current.value, end=" ")
    current = current.next

