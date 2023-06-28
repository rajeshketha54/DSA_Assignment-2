# Merge a linked list into another linked list at alternate positions.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def merge_lists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    current1 = list1
    current2 = list2

    while current1 and current2:
        temp = current1.next
        current1.next = current2
        current2 = current2.next
        current1.next.next = temp
        current1 = temp

    return list1

list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(3)

list2 = Node(4)
list2.next = Node(5)
list2.next.next = Node(6)

merged_list = merge_lists(list1, list2)
current = merged_list
while current:
    print(current.value, end=" ")
    current = current.next

