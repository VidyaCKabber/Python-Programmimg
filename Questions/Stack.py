a = [[1], (2, [3, 66, 9, {4: 8}], 3), {4: 2, 7: 6}, [4, 5, 6, 7]]
res = []

stack = list(a)  # Initialize the stack with the top-level elements

print(stack)

while stack:
    item = stack.pop(0)  # Get the next item from the stack
    print("-------item---------")
    print(item)
    
    if isinstance(item, dict):
        # Extend the stack with dictionary keys and values
        stack.extend(list(item.items()))
    elif isinstance(item, (list, tuple)):
        # Extend the stack with elements of the list or tuple
        stack.extend(item)
    else:
        # Directly add non-container items to the result
        res.append(item)
