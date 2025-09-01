# Solution.py

"""
Python solutions for Day 17: Stack & Queue problems.
This file includes implementations for:
1. A Stack using a list.
2. A Queue using two stacks.
3. A function to check for balanced parentheses.
4. A Circular Queue.
5. A function to find the Next Greater Element in an array.
"""

from typing import List, Any, Optional

# ==============================================================================
# Problem 1: Implement a Stack using a List
# ==============================================================================

class Stack:
    """
    A LIFO (Last-In, First-Out) stack implementation using a Python list.
    """
    def __init__(self):
        """Initializes an empty stack."""
        self._items: List[Any] = []

    def is_empty(self) -> bool:
        """Checks if the stack is empty."""
        return not self._items

    def push(self, item: Any):
        """
        Adds an item to the top of the stack.
        Time Complexity: O(1) on average.
        """
        self._items.append(item)

    def pop(self) -> Any:
        """
        Removes and returns the item from the top of the stack.
        Raises an IndexError if the stack is empty.
        Time Complexity: O(1).
        """
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._items.pop()

    def peek(self) -> Any:
        """
        Returns the item at the top of the stack without removing it.
        Raises an IndexError if the stack is empty.
        Time Complexity: O(1).
        """
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self._items[-1]

    def size(self) -> int:
        """Returns the number of items in the stack."""
        return len(self._items)


# ==============================================================================
# Problem 2: Implement a Queue using Two Stacks
# ==============================================================================

class QueueWithStacks:
    """
    A FIFO (First-In, First-Out) queue implementation using two stacks.
    This implementation achieves amortized O(1) time complexity for its operations.
    """
    def __init__(self):
        """Initializes two stacks for the queue implementation."""
        self.in_stack: List[Any] = []  # Used for enqueuing
        self.out_stack: List[Any] = [] # Used for dequeuing

    def _transfer_if_needed(self):
        """
        Transfers elements from in_stack to out_stack if out_stack is empty.
        This reversal is the key to simulating FIFO behavior with two LIFO stacks.
        """
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def enqueue(self, item: Any):
        """
        Adds an item to the back of the queue.
        Time Complexity: O(1).
        """
        self.in_stack.append(item)

    def dequeue(self) -> Any:
        """
        Removes and returns the item from the front of the queue.
        Raises an IndexError if the queue is empty.
        Time Complexity: Amortized O(1).
        """
        self._transfer_if_needed()
        if not self.out_stack:
            raise IndexError("dequeue from an empty queue")
        return self.out_stack.pop()

    def is_empty(self) -> bool:
        """Checks if the queue is empty."""
        return not self.in_stack and not self.out_stack


# ==============================================================================
# Problem 3: Balanced Parentheses Checker
# ==============================================================================

def is_balanced(s: str) -> bool:
    """
    Checks if a string of parentheses '()[]{}' is balanced using a stack.

    Args:
        s: The input string containing parentheses.

    Returns:
        True if the string is balanced, False otherwise.
    
    Time Complexity: O(n) where n is the length of the string.
    Space Complexity: O(n) in the worst case (e.g., "((((...))))").
    """
    stack = []
    # A mapping of closing brackets to their corresponding opening ones.
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map.values():
            # If it's an opening bracket, push it onto the stack.
            stack.append(char)
        elif char in bracket_map:
            # If it's a closing bracket:
            # 1. The stack cannot be empty.
            # 2. The top of the stack must be the matching opening bracket.
            if not stack or stack.pop() != bracket_map[char]:
                return False
    
    # After iterating, a balanced string means the stack must be empty.
    return not stack


# ==============================================================================
# Problem 4: Circular Queue Implementation
# ==============================================================================

class CircularQueue:
    """
    A fixed-size circular queue (ring buffer) implementation using a list.
    """
    def __init__(self, k: int):
        """
        Initializes the circular queue with a fixed capacity.
        
        Args:
            k: The maximum size of the queue.
        """
        self.queue: List[Optional[int]] = [None] * k
        self.capacity = k
        self.head = 0  # Points to the front of the queue
        self.tail = 0  # Points to the next available slot at the rear
        self.count = 0 # Current number of elements in the queue

    def is_empty(self) -> bool:
        """Checks if the queue is empty."""
        return self.count == 0

    def is_full(self) -> bool:
        """Checks if the queue is full."""
        return self.count == self.capacity

    def enqueue(self, value: int) -> bool:
        """
        Inserts an element into the rear of the queue.
        Returns True on success, False if the queue is full.
        Time Complexity: O(1).
        """
        if self.is_full():
            return False
        self.queue[self.tail] = value
        # Move tail pointer in a circular fashion
        self.tail = (self.tail + 1) % self.capacity
        self.count += 1
        return True

    def dequeue(self) -> int:
        """
        Deletes and returns the element from the front of the queue.
        Returns -1 if the queue is empty.
        Time Complexity: O(1).
        """
        if self.is_empty():
            return -1
        value = self.queue[self.head]
        # Move head pointer in a circular fashion
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return value


# ==============================================================================
# Problem 5: Next Greater Element
# ==============================================================================

def next_greater_element(arr: List[int]) -> List[int]:
    """
    Finds the Next Greater Element (NGE) for each element in an array.

    Args:
        arr: The input list of integers.

    Returns:
        A list where each element is the NGE of the corresponding element
        in the input array. If no NGE exists, it is -1.

    Time Complexity: O(n) as each element is pushed and popped once.
    Space Complexity: O(n) for the stack and result array.
    """
    n = len(arr)
    result = [-1] * n
    # The stack will store indices of elements awaiting their NGE.
    stack = []

    # Iterate through the array from left to right.
    for i in range(n):
        # While stack is not empty and the current element is greater
        # than the element at the index on top of the stack...
        while stack and arr[i] > arr[stack[-1]]:
            # The current element is the NGE for the element at stack's top index.
            top_index = stack.pop()
            result[top_index] = arr[i]
        
        # Push the current index onto the stack, as it awaits its own NGE.
        stack.append(i)
        
    return result


# ==============================================================================
# Test Cases
# ==============================================================================

if __name__ == "__main__":
    print("--- Testing Problem 1: Stack ---")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print(f"Peek: {stack.peek()}")  # Expected: 20
    stack.push(30)
    print(f"Popped: {stack.pop()}") # Expected: 30
    print(f"Size: {stack.size()}")  # Expected: 2
    print(f"Popped: {stack.pop()}") # Expected: 20
    print(f"Is Empty: {stack.is_empty()}") # Expected: False
    print("-" * 30)

    print("\n--- Testing Problem 2: Queue with Two Stacks ---")
    q_stacks = QueueWithStacks()
    q_stacks.enqueue(1)
    q_stacks.enqueue(2)
    q_stacks.enqueue(3)
    print(f"Dequeued: {q_stacks.dequeue()}") # Expected: 1
    print(f"Dequeued: {q_stacks.dequeue()}") # Expected: 2
    q_stacks.enqueue(4)
    print(f"Dequeued: {q_stacks.dequeue()}") # Expected: 3
    print(f"Dequeued: {q_stacks.dequeue()}") # Expected: 4
    print(f"Is Empty: {q_stacks.is_empty()}") # Expected: True
    print("-" * 30)

    print("\n--- Testing Problem 3: Balanced Parentheses ---")
    print(f"'()[]{{}}' is balanced: {is_balanced('()[]{}')}")  # Expected: True
    print(f"'([)]' is balanced: {is_balanced('([)]')}")    # Expected: False
    print(f"'{{[]}}' is balanced: {is_balanced('{[]}')}")     # Expected: True
    print(f"'(' is balanced: {is_balanced('(')}")           # Expected: False
    print(f"')' is balanced: {is_balanced(')')}")           # Expected: False
    print(f"'' is balanced: {is_balanced('')}")           # Expected: True
    print("-" * 30)

    print("\n--- Testing Problem 4: Circular Queue ---")
    cq = CircularQueue(3)
    print(f"Enqueue 1: {cq.enqueue(1)}") # Expected: True
    print(f"Enqueue 2: {cq.enqueue(2)}") # Expected: True
    print(f"Enqueue 3: {cq.enqueue(3)}") # Expected: True
    print(f"Is Full: {cq.is_full()}")      # Expected: True
    print(f"Enqueue 4: {cq.enqueue(4)}") # Expected: False
    print(f"Dequeue: {cq.dequeue()}")     # Expected: 1
    print(f"Is Full: {cq.is_full()}")      # Expected: False
    print(f"Enqueue 4: {cq.enqueue(4)}") # Expected: True
    print(f"Dequeue: {cq.dequeue()}")     # Expected: 2
    print(f"Dequeue: {cq.dequeue()}")     # Expected: 3
    print(f"Dequeue: {cq.dequeue()}")     # Expected: 4
    print(f"Is Empty: {cq.is_empty()}")   # Expected: True
    print(f"Dequeue from empty: {cq.dequeue()}") # Expected: -1
    print("-" * 30)

    print("\n--- Testing Problem 5: Next Greater Element ---")
    arr1 = [4, 5, 2, 25]
    print(f"Array: {arr1}, NGE: {next_greater_element(arr1)}")
    # Expected: [5, 25, 25, -1]
    
    arr2 = [13, 7, 6, 12]
    print(f"Array: {arr2}, NGE: {next_greater_element(arr2)}")
    # Expected: [-1, 12, 12, -1]
    
    arr3 = [1, 2, 3, 4, 5]
    print(f"Array: {arr3}, NGE: {next_greater_element(arr3)}")
    # Expected: [2, 3, 4, 5, -1]
    
    arr4 = [5, 4, 3, 2, 1]
    print(f"Array: {arr4}, NGE: {next_greater_element(arr4)}")
    # Expected: [-1, -1, -1, -1, -1]
    print("-" * 30)
