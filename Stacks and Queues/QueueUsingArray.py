# Check if the Queue is empty or not 
def isEmpty(queue):
    return True if not queue else False

def peek(queue):
    if isEmpty(queue):
        print("Queue is Empty!")
        return
    
    return queue[0]

# enqueue an item onto the top of the queue.
def enqueue(queue, data):
    queue.append(data)

# Remove and return the bottom item from the queue.
def dequeue(queue):
    if isEmpty(queue):
        print("Queue Underflow.")
        return
    
    queue.pop(0)

# Create an empty queue.
queue = []

# Insert some values into the queue.
enqueue(queue, 5)
enqueue(queue, 78)
enqueue(queue, 3)
enqueue(queue, 10)
enqueue(queue, 8)

# Queue before pop 
print(f"Queue before dequeue: {queue}")
# Remove the bottom element.
dequeue(queue)
dequeue(queue)

# Display the current queue from bottom to top.
print(f"Queue after dequeue: {queue}")
print(f"peek: {peek(queue)}")
print("Empty Queue: ", isEmpty(queue))