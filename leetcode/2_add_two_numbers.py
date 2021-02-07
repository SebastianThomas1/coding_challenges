# 2. Add Two Numbers
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their
# nodes contains a single digit. Add the two numbers and return the sum
# as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except
# the number 0 itself.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(head1: ListNode, head2: ListNode) -> ListNode:
    carry = 0

    head = ListNode()

    current = head
    while head1 or head2 or carry:
        val1 = head1.val if head1 else 0
        val2 = head2.val if head2 else 0

        carry, value = divmod(val1 + val2 + carry, 10)
        current.next = ListNode(val=value)

        head1 = head1.next if head1 else None
        head2 = head2.next if head2 else None
        current = current.next

    return head.next


def head_of(lst):
    if not lst:
        return None

    head = ListNode(val=lst[0])

    current_node = head
    for value in lst[1:]:
        current_node.next = ListNode(val=value)
        current_node = current_node.next

    return head


def as_list(head):
    if not head:
        return []

    lst = []

    current_node = head
    while current_node:
        lst.append(current_node.val)
        current_node = current_node.next

    return lst


if __name__ == '__main__':
    print(as_list(add_two_numbers(head_of([2, 4, 3]), head_of([5, 6, 4]))))
    # [7, 0, 8]
    print(as_list(add_two_numbers(head_of([0]), head_of([0]))))
    # [0]
    print(as_list(add_two_numbers(head_of([9, 9, 9, 9, 9, 9, 9]),
                                  head_of([9, 9, 9, 9]))))
    # [8,9,9,9,0,0,0,1]
