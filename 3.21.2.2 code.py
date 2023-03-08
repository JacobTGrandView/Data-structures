# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 09:09:09 2022

@author: jt108
"""




class Node:
    """A node of a linked list"""

    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        """Get node data"""
        return self._data

    def set_data(self, node_data):
        """Set node data"""
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        """Get next node"""
        return self._next

    def set_next(self, node_next):
        """Set next node"""
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self):
        """String"""
        return str(self._data)


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next

        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next

        return False

    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        if current is None:
            raise ValueError("{} is not in the list".format(item))
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
     
###################### insert, apppend, index, pop ###########################
            
    def pop(self): ################# POP ###########
        current = self.head
        previous = None
    
        while current.get_next() != None:
            previous = current
            current = current.get_next()
    
        previous.set_next(None)
        return current.get_data()
    
    def add(self, item): ############ ADD ############
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        
    def append(self, item): ########## APPEND ############
        current = self.head
        temp = Node(item)
        while current != None:
            current = current.get_next()
    
        current.set_next(temp)
        
    def index(self, item): ############## INDEX #################
        current = self.head
        found = False
        index = 0
        
        while current != None and not found:
            if current.get_data() != item:
                index +=1
                current = current.get_next()
            else:
                found = True
        
            if found:
                return index
            else:
                return "Index Not Found"
            
my_list = UnorderedList()
my_list.add('hello')
print(my_list.index('hello'))

            


       
        
    