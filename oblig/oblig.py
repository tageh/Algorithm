#!/usr/bin/env python3
#TODO: Own function for checking and printing that the list is empty


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head, self.tail = None, None

    def deleteFirstNode(self):
        self.head = self.head.next

    def addEndNode(self, data):
        newNode = Node(data)
        
        # If there are no nodes
        if self.head is None: 
            self.head = newNode
            self.tail = newNode
            return

        if self.head is not None:
            newNode.prev = self.tail
            # Access the last node and make it's next value set to the newly created node
            self.tail.next = newNode 
            self.tail = newNode

    def deleteLastNode(self):
        self.tail = self.tail.prev
        self.tail.next = None

    # Task 4 - Delete all nodes with specified value
    def deleteSelectedValue(self, value):
        current = self.head
        if current is None:
            print("List is empty")
            return

        # TODO: Rename X Value
        # Important concept: A node is deleted when there is no other nodes pointing to it
        def deleteCurrentNode(node): # Gets the node to be deleted
            # Since it's a doubly list, the node has two "connections" that needs to be rewired
            # - The previous node needs to point to the next(next) node
            # - The next node next to point to the previous(previous) node
            if node.prev is None: # If we are on the first node we have to manipulate the head
                self.head = node.next
            else:
                x = node.prev # Go one node back
                x.next = node.next # Could also be x.next.next

            if node.next is None: # If we are on the last node we have to manipulate the tail
                self.tail = node.prev
            else: 
                x = node.next # Go to the next node
                x.prev = node.prev # Could also be x.prev.prev
            return

        while current is not None: # Traverse through entire list, delete nodes that match
            if value == current.value:
                deleteCurrentNode(current)
            current = current.next

    # Task 5 - Add an item after an item with the specified value.
    # TODO: Fix that a user can add a value after the same value
    def addItemAfterValue(self, nodeValue, insertValue):
        # Find nodes with the specified value
        # Insert a node after it
        
        current = self.head
        if current is None:
            print("List is empty")
            return
        
        while current is not None:
            newNode = Node(insertValue)
            if current.data == nodeValue:
                # Insert node after
                # The current node needs to point at the new node
                # The node after the new node needs to point to the new node
                if current.next is not None:
                    x = current.next # This is none
                    newNode.next = x
                    current.next = newNode
                    newNode.prev = current
                    x = current.next
                    x.prev = newNode
                
                if current.next is None: # If we are on tail, update the tail
                    self.tail = newNode
                    current.next = newNode
                    newNode.prev = current
                   
            current = current.next       


    # Task 6 - Add an item in front of an item with the specified value
    def addItemBeforeValue(self, nodeValue, insertValue):
        # Find nodes with the specified value
        # Insert a node after it
        
        current = self.tail

        if current is None:
            print("List is empty")
            return
        
        while current is not None:
            newNode = Node(insertValue)
            if current.data == nodeValue:
                if current.prev is not None:
                    x = current.prev # This is none
                    newNode.prev = x
                    current.prev = newNode
                    newNode.next = current
                    x = current.prev.prev
                    x.next = newNode
                
                if current.prev is None: # If we are on tail, update the tail
                    self.head = newNode
                    current.prev = newNode
                    newNode.next = current
                    
            current = current.prev       

    # Task 7 - Print the length of the list
    def printLength(self):
        current = self.head
        if current is None:
            print("List is empty")
            return

        count = 0
        while current is not None:
            current = current.next
            count += 1
        return count

    # Task 8 - Count the number of occurrences of element with given value in the list, this number is printed
    def countNumberOfOccurrences(self, value):
        current = self.head
        if current is None:
            print("List is empty")
            return
        
        count = 0
        while current is not None:
            if current.data == value:
                count += 1

            current = current.next
        return count


    # Task 9 - Print entire list
    def print(self, backwards = False):
        # Check if there is a node in the list
        current = self.head
        if current is None:
            print("Empty list")
            return
        
        if backwards is True: # If backwards is set to True print the list backwards
            current = self.tail
            while current is not None:
                print(current.data)
                current = current.prev
        else: 
            while current is not None:
                print(current.data)
                current = current.next

                
    # Task 10 - Delete the entire list. How many items were deleted is printed
    def deleteList(self):
        current = self.head
        if current is None:
            print("List is empty")
            return
        count = 0
        while current is not None:
            self.head = None
            self.tail = None
            current = current.next
            count += 1
        return count
