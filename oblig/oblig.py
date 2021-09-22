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
        return

    def addEndNode(self, data):
        newNode = Node(data)
        
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

    def deleteLastNode(self):
        self.tail = self.tail.prev
        self.tail.next = None
        return

    def deleteNodesWithValue(self, value):
        curr = self.head
        if curr is None:
            print("List is empty")
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

    # TODO: Fix that a user can add a value after the same value
    def addNodeAfterValue(self, val, insVal):
        current = self.head

        if current is None:
            print("List is empty")
            return
        
        while current is not None:
            newNode = Node(insVal)
            if current.data == val:
                if current.next is not None:
                    tmp = current.next
                    newNode.next = tmp
                    current.next = newNode
                    newNode.prev = current
                    tmp.prev = newNode
                    current = current.next.next
                    continue
                
                # If on last node, update tail
                if current.next is None:
                    self.tail = newNode
                    current.next = newNode
                    newNode.prev = current
                    break
            current = current.next
        return   


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
