#!/usr/bin/env python3

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
    def deleteSelectedValue(self, data):
        current = self.head
        if current is None:
            print("List is empty")
            return
       
        if current is data:
            self.deleteFirst()

        while current.next is not data:
            current = current.next
            break
        
        print(str(current.data) + "\n")
        #current.next = current.next.next
        #current.next.next = current




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

list.addEnd(1)
list.addEnd(2)
list.addEnd(3)
list.addEnd(4)
list.addEnd(5)
list.addEnd(6)
list.addEnd(7)

# list.deleteSelectedValue(2)
list.deleteFirst()
list.print()

print("Head: " + str(list.head.data))
print("Tail: " + str(list.tail.data))
print("Prev Tail: " + str(list.tail.prev.data))
