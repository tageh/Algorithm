#!/usr/bin/env python3
from Node import Node
class LinkedList:
    def __init__(self, Node):
        self.head, self.tail = None, None
        self.Node = Node

    def get_option_list(self):
        return [
            "Delete an item first in the list",
            "Add an item to the end of the list",
            "Delete an item at the end of the list",
            "Delete an item with the specified value from the list",
            "Add an item after an item with the specified value",
            "Add an item in front of an item with the specified value",
            "Print the length of the list",
            "Count the number of occurrences of element with given value in the list, this number is printed",
            "Print the entire list (9b for backwards)",
            "Delete the entire list. How many items were deleted is printed",
            "Quickly generate a large list"
        ]


    def empty_list(self, node):
        if node is None:
            print("List is empty")
            return True
        return False

    def delete_first_node(self):
        self.head = self.head.next
        return

    def add_end_node(self, data):
        newNode = self.node(data)
        
        # If there are no nodes
        if self.head is None: 
            self.head = newNode
            self.tail = newNode
            return

        if self.head is not None:
            newNode.prev = self.tail
            # Access the last node and make next value same as newly created node
            self.tail.next = newNode 
            self.tail = newNode
        return

    def delete_last_node(self):
        self.tail = self.tail.prev
        self.tail.next = None
        return

    def delete_nodes_with_value(self, value):
        curr = self.head

        if self.emptyList(curr):
            return

        while curr is not None:
            if value == curr.data:
                # If previous node doesn't exist, move head
                if curr.prev is None:
                    self.head = curr.next
                
                # If next node doesn't exist, move tail
                if curr.next is None:
                    self.tail = curr.prev

                if curr.prev is not None:
                    tmp = curr.prev
                    tmp.next = curr.next
                
                if curr.next is not None:
                    tmp = curr.next
                    tmp.prev = curr.prev
            curr = curr.next.next
        return

    def add_node_after_value(self, val, insVal):
        curr = self.head

        if self.emptyList(curr):
            return
        
        while curr is not None:
            newNode = self.node(insVal)
            if curr.data == val:
                if curr.next is not None:
                    tmp = curr.next
                    newNode.next = tmp
                    curr.next = newNode
                    newNode.prev = curr
                    tmp.prev = newNode
                    curr = curr.next.next
                    continue
                
                # If on last node, update tail
                if curr.next is None:
                    self.tail = newNode
                    curr.next = newNode
                    newNode.prev = curr
                    break
            curr = curr.next
        return   

    def add_node_before_value(self, val, insVal):
        curr = self.tail

        if self.emptyList(curr):
            return
        
        while curr is not None:
            newNode = self.node(insVal)
            if curr.data == val:
                if curr.prev is not None:
                    tmp = curr.prev
                    newNode.prev = tmp
                    curr.prev = newNode
                    newNode.next = curr
                    tmp.next = newNode
                    curr = curr.prev.prev
                    continue
                
                # If on first node, update head
                if curr.prev is None:
                    self.head = newNode
                    curr.prev = newNode
                    newNode.next = curr
                    break
            curr = curr.prev
        return   

    
    def list_length(self):
        curr = self.head
        count = 0

        if self.emptyList(curr):
            return

        while curr is not None:
            curr = curr.next
            count += 1
        return count

    def count_occourences(self, value):
        curr = self.head
        count = 0
        
        if self.emptyList(curr):
            return
        
        while curr is not None:
            if curr.data == value:
                count += 1

            curr = curr.next
        return count


    def print_list(self, backwards = False):
        curr = self.head
        
        if self.emptyList(curr):
            return
        
        if backwards is True:
            curr = self.tail
            while curr is not None:
                print(curr.data)
                curr = curr.prev
        else: 
            while curr is not None:
                print(curr.data)
                curr = curr.next
        return

                
    def delete_list(self):
        curr = self.head
        count = 0

        if self.emptyList(curr):
            return

        while curr is not None:
            self.head = None
            self.tail = None
            curr = curr.next
            count += 1
        return count
