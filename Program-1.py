class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_zero_sum(head):
    dummy = Node(0)
    dummy.next = head
    prefix_sum = 0
    prefix_sum_map = {}
    current = dummy

    while current:
        prefix_sum += current.data

        if prefix_sum in prefix_sum_map:
            prev = prefix_sum_map[prefix_sum].next
            temp_sum = prefix_sum + prev.data

            while prefix_sum != temp_sum:
                prefix_sum -= prev.next.data
                prev.next = prev.next.next

            prefix_sum_map[prefix_sum].next = current.next
        else:
            prefix_sum_map[prefix_sum] = current

        current = current.next

    return dummy.next

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

def create_linked_list(nums):
    head = None
    tail = None

    for num in nums:
        if not head:
            head = Node(num)
            tail = head
        else:
            new_node = Node(num)
            tail.next = new_node
            tail = new_node

    return head

nums = [3, -3, 2, -2, 5]
head = create_linked_list(nums)

print("Original Linked List:")
print_linked_list(head)

head = delete_zero_sum(head)

print("Modified Linked List:")
print_linked_list(head)
