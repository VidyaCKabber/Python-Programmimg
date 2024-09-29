class MyQueue:

    def __init__(self):
        self.stack = []
        self.front_index = 0
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return None
        pop_element = self.stack[self.front_index]
        self.front_index +=1
        
        if self.front_index > len(self.stack) // 2:  # Check if more than half of the elements are popped
            self.stack = self.stack[self.front_index:]  # Remove elements up to the front index
            self.front_index = 0  # Reset the front index
        return pop_element

        
    def peek(self) -> int:
        if not self.stack:
            return None
        return self.stack[self.front_index]
        

    def empty(self) -> bool:
        return self.front_index >= len(self.stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
