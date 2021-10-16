"""
    Author: Urveshkumar Patel
    GitHub: https://github.com/urvesh254
"""


class Node:
    """It is a representation of the LinkedList node."""

    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


def reverseLL(head) -> Node:
    """
    Efficient method for reversing the LinkedList.

    Time Complexity: O(n)
    Space Complexity: O(1)

    @param head Start pointer of the LinkedList.
    @return Updated head after reversing the LinkedList.
    """

    pre, curr, next = None, head, None
    while curr:
        pre = curr.next
        curr.next = next
        next = curr

        curr = pre

    return next


""" Uncomment below code for Testing """

"""
def displayLL(head):
    q = head
    while q:
        print(q.data, end="->")
        q = q.next
    print()


head = Node("1")
head.next = Node("2")
head.next.next = Node("3")
head.next.next.next = Node("4")
head.next.next.next.next = Node("5")
head.next.next.next.next.next = Node("6")

displayLL(head)
displayLL(reverseLL(head))
"""
