# Node structure for a linked-list-based queue.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue implementation using a singly linked list.
class Queue:
    def __init__(self):
        # front points to the front of the queue
        # rear points to the rear of the queue
        self.front = None
        self.rear = None

    # Check whether the queue is empty.
    def isEmpty(self):
        return self.front is None

    # Insert an element at the end (rear) of the queue.
    def enqueue(self, data):
        newNode = Node(data)

        # If the queue is empty, both front and rear point to the new node.
        if self.rear is None:
            self.front = self.rear = newNode
            print(f"Enqueued {data}")
            return

        # Otherwise, attach the new node at the end and update the rear.
        self.rear.next = newNode
        self.rear = newNode
        print(f"Enqueued {data}")

    # Remove the front element from the queue.
    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow (Empty)")
            return

        dequeued_node = self.front
        self.front = self.front.next

        # If the queue becomes empty, reset the rear pointer as well.
        if self.front is None:
            self.rear = None
        print("Dequeued ", dequeued_node.data)

    # Look at the front element without removing it.
    def peek(self):
        if self.isEmpty():
            print("Queue is Empty.")
            return
        print(f"front element(peek): {self.front.data}")

    # Display all queue elements from front to rear.
    def display(self):
        if self.isEmpty():
            print("Queue is Empty.")
            return

        curr = self.front
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")


if __name__ == "__main__":
    # Create a queue and insert some values.
    queue = Queue()

    queue.enqueue(12)
    queue.enqueue(23)
    queue.enqueue(7)
    queue.enqueue(43)
    queue.enqueue(23)

    print()
    print("Initial Queue: ")
    queue.display()
    print()

    # Remove two items from the front of the queue.
    queue.dequeue()
    queue.dequeue()

    print()
    print("After Dequeue: ")
    queue.display()
    print()

    # See the front item without deleting it.
    queue.peek()
    