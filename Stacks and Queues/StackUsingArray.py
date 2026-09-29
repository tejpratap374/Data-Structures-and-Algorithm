# Check if the stack is empty or not 
def isEmpty(stack):
    return True if not stack else False

# Display the element at top 
def peek(stack):
    if isEmpty(stack):
        print("Stack is Empty!")
        return
    
    return stack[-1]
        
# Push an item onto the top of the stack.
def push(stack, data):
    stack.append(data)

# Remove and return the top item from the stack.
def pop(stack):
    if isEmpty(stack):
        print("Stack Underflow.")
        return
    
    stack.pop()

# Create an empty stack.
stack = []

# Insert some values into the stack.
push(stack, 5)
push(stack, 3)
push(stack, 10)
push(stack, 6)

# Stacck Before Pop
print("Bottom to Top: ")
print("Before Pop: ", stack)
 
# Remove the top element.
pop(stack)

# Display the current stack from bottom to top.
print("After Pop: ", stack)
print(f"Empty stack?: {isEmpty(stack)}")
print(f"Top element: {peek(stack)}")