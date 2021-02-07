# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list
#
# Delete a Node

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def delete_node(head, position):
    if position == 0:
        return head.next
    else:
        current_node = head
        while position != 1:
            current_node = current_node.next
            position -= 1

        current_node.next = current_node.next.next

        return head
