# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 12:29:32 2022

@author: jt108
"""

#Build a stack class from scratch (chapter 3.5)
#Build a stack in python using four different items of your choice
#Remove the top item
#Return the size of the stack
#Return the top item without removing it


class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create new stack"""
        self._items = []

    def is_empty(self):
        """Check if the stack is empty"""
        return not bool(self._items)

    def push(self, item):
        """Add an item to the stack"""
        self._items.append(item)

    def pop(self):
        """Remove an item from the stack"""
        return self._items.pop()

    def peek(self):
        """Get the value of the top item in the stack"""
        return self._items[-1]

    def size(self):
        """Get the number of items in the stack"""
        return len(self._items)

MyStack = Stack()


MyStack.push('9') #Add 9 to the stack
MyStack.push('10') #Add 10 to the stack
MyStack.push('11') #Add 11 to the stack
MyStack.push('12') #Add 12 to the stack
MyStack.pop() #Remove the top item from the stack, 12 is the top item
print(MyStack.size()) #Shows the size of the stack, which is 3
print(MyStack.peek()) #Shows the top item on the stack, which is 11





