# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list
#
# Delete duplicate-value nodes from a sorted linked list

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def remove_duplicates(head):
    if head is None:
        return None

    current_node = head
    while current_node.next:
        if current_node.data == current_node.next.data:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next

    return head
