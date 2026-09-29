# Node class for the linked-list implementation of a stack.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack implementation using a singly linked list.
class Stack:
    def __init__(self):
        # top points to the last inserted element.
        self.top = None

    # Return True if the stack is empty; otherwise False.
    def isEmpty(self):
        return self.top is None

    # View the top element without removing it.
    def peek(self):
        if not self.isEmpty:
            print("Queue is Empty.")
            return

        print(f"Top element(peek): {self.top.data}")

    # Insert a new value at the top of the stack.
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.top   # new node points to previous top
        self.top = newNode        # update top to new node
        print(f"pushed {data} to stack.")

    # Remove the top element from the stack.
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow.")
            return

        print(f"Poped element: {self.top.data}")
        self.top = self.top.next

    # Display all elements from top to bottom.
    def display(self):
        if self.top is None:
            print("Stack is Empty.")
            return

        curr = self.top
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None\n")


if __name__ == "__main__":
    # Create a new stack.
    stack = Stack()

    # Push elements into the stack.
    stack.push(4)
    stack.push(8)
    stack.push(9)
    stack.push(34)
    stack.push(12)

    print("\nBefore Pop: ")
    stack.display()

    # Remove the top item and inspect the stack.
    stack.pop()
    stack.peek()
    print(f"Stack Empty?: {stack.isEmpty()}")

    print("\nAfter pop: ")
    stack.display()