#!/usr/bin/env python3
#TODO: Own function for checking and printing that the list is empty


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Task 1 - Delete the first node
    def deleteFirst(self):
        self.head = self.head.next

    # Task 2 Add one node to the end of the list
    def addEnd(self, data):
        newNode = Node(data)
        
        if self.head is None: # If there are no nodes in the list make head and tail point to newly created node
            self.head = newNode
            self.tail = newNode
            return

        if self.head is not None: # If there are nodes in the list
            newNode.prev = self.tail # The new nodes previous value should be the current tail
            self.tail.next = newNode # Access the last node and make it's next value set to the newly created node
            newNode.prev = self.tail # Newnode points to the previous node (since we have a doubly list)
            self.tail = newNode # Set the tail variable to the new node

    # Task 3 - Delete the last node
    def deleteLast(self):
        self.tail = self.tail.prev # Set the tail to the previous node
        self.tail.next = None # Set the previous node's next pointer to null

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
    def addItemAfterValue(self, nodeValue, insertValue ):
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
                    
                
                
                # print(self.tail.prev.data)
                # print("HERE FUCKER")

            current = current.next       


    # Task 6 - Add an item in front of an item with the specified value
    def addItemBeforeValue(self, nodeValue, insertValue ):
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
                    
                
                
                # print(self.tail.prev.data)
                # print("HERE FUCKER")

            current = current.prev       

    # Task 7 - Print the length of the list
    def printLength(self):
        current = self.head
        count = 0
        while current is not None:
            current = current.next
            count += 1
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

        
            
# Testing

list = LinkedList()

list.addEnd(2)
list.addEnd(1)
list.addEnd(2)
list.addEnd(3)
list.addEnd(4)
list.addEnd(5)
list.addEnd(2)
list.addEnd(6)
list.addEnd(10)
list.addEnd(2)

#list.deleteSelectedValue(2)
#list.deleteFirst()
#list.addItemAfterValue(2, 2012512)
list.addItemBeforeValue(2, 2012512)
#list.print()
print("Length is: " + str(list.printLength()))

print("Head: " + str(list.head.data))
print("Tail: " + str(list.tail.data))
print("Next Head: " + str(list.head.next.data))
print("Prev Tail: " + str(list.tail.prev.data))
