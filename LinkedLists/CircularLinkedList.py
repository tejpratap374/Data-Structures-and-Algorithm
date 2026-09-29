'''
Circular linked list implementation with insertion and deletion operations.

Operations covered:
- insert at the beginning
- insert at the end
- insert at a given position
- delete from the beginning
- delete from the end
- delete from a given position

The tail pointer always points to the last node in the circular list. The list is
considered empty when the tail is None.
'''


class Node:
    """Node for a circular linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


def insertAtBegining(tail, data):
    """Insert a new node at the front of the circular list.

    If the list is empty, the new node becomes the only node and points to itself.
    Otherwise, the new node is placed before the current head and the tail stays
    unchanged.
    """
    newNode = Node(data)

    # Empty list: the new node points to itself and becomes the only node.
    if tail is None:
        newNode.next = newNode
        return newNode

    # Insert before the current head while keeping the tail pointer unchanged.
    newNode.next = tail.next
    tail.next = newNode
    return tail


def insertAtEnd(tail, data):
    """Insert a new node at the end of the circular list.

    The new node becomes the new tail and its next pointer points back to the head.
    """
    newNode = Node(data)

    # Empty list: create the first circular node.
    if tail is None:
        newNode.next = newNode
        return newNode

    # Attach the new node right after the current tail and update tail to it.
    newNode.next = tail.next
    tail.next = newNode
    return newNode


def inserrtAtPosition(tail, position, data):
    """Insert data at a 1-based position in the circular list.

    If the position is invalid or out of range, the element is appended at the end.
    """
    if position <= 1 or tail is None:
        return insertAtBegining(tail, data)

    head = tail.next
    curr = head

    for _ in range(1, position - 1):
        curr = curr.next
        if curr == head:
            print(f"position {position} out of bound, appending {data} at the end.")
            return insertAtEnd(tail, data)

    if curr == tail:
        return insertAtEnd(tail, data)

    newNode = Node(data)
    newNode.next = curr.next
    curr.next = newNode
    return tail


def deleteBegining(tail):
    """Delete the first node of the circular list.

    If the list contains one element, removing it makes the list empty and returns None.
    """
    # Empty list: nothing to delete.
    if tail is None:
        print("List is Empty.")
        return None

    head = tail.next

    # Only one node exists: removing it leaves the list empty.
    if head is tail:
        return None

    # Move the tail's next pointer to skip the head node.
    tail.next = head.next
    return tail


def deleteEnd(tail):
    """Delete the last node of the circular list and return the new tail."""
    # Empty list: nothing to delete.
    if tail is None:
        print("List is Empty.")
        return None

    head = tail.next

    # Single-node list becomes empty.
    if head is tail:
        return None

    # Two-node list: the head becomes the new tail and points to itself.
    if head.next == tail:
        head.next = head
        return head

    # Traverse to the node just before the tail and remove the tail.
    curr = head
    while curr.next != tail:
        curr = curr.next

    curr.next = tail.next
    return curr


def deletePos(tail, pos):
    """Delete the node at a 1-based position from the circular list.

    If the position is invalid, the function removes the last element.
    """
    if tail is None:
        print("List is Empty.")
        return None

    if pos <= 1:
        return deleteBegining(tail)

    head = tail.next
    curr = head

    for _ in range(1, pos - 1):
        curr = curr.next
        if curr == head:
            print(f"position {pos} is out of bound, deleting from end.")
            return deleteEnd(tail)

    if curr.next == tail:
        return deleteEnd(tail)

    curr.next = curr.next.next
    return tail


def printList(tail):
    """Print all nodes in the circular list from the head to the tail."""
    # Empty list: show a clear message.
    if tail is None:
        print("List is Empty.")
        return

    # Start from the head, which is always stored as tail.next.
    head = tail.next
    curr = head

    # Keep printing until we loop back to the head.
    while True:
        print(f"{curr.data}", end=" -> ")
        if curr.next == head:
            break
        curr = curr.next

    print("head")

if __name__ == "__main__":
    # Basic demonstration of the operations requested in the problem statement.
    tail = None

    # Insert at beginning
    tail = insertAtBegining(tail, 4)
    tail = insertAtBegining(tail, 6)

    # Insert at end
    tail = insertAtEnd(tail, 8)

    # Insert in the middle
    tail = inserrtAtPosition(tail, 6, 9)
    tail = inserrtAtPosition(tail, 3, 7)

    print("After insertions:")
    printList(tail)

    # Delete from the beginning
    tail = deleteBegining(tail)

    # Delete from the end
    tail = deleteEnd(tail)

    # Delete from the middle
    tail = deletePos(tail, 2)
    tail = deletePos(tail, -4)

    print("After deletions:")
    printList(tail)