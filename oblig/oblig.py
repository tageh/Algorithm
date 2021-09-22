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

    #Task 1
    def deleteFirst(self):
        self.head = self.head.next
        self.head.prev = None

    #Task 2
    def addEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return

        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode

    #Task 3
    def deleteLast(self):
        self.tail = self.tail.prev
        self.tail.next = None

    #Task 4
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




    #Task 9
    def print(self):
        current = self.head
        if current is None:
            print("Empty list")
            return

        while current is not None:
            print(current.data)
            current = current.next
            

liste = LinkedList()

liste.addEnd(1)
liste.addEnd(2)
liste.addEnd(3)
liste.addEnd(4)
liste.addEnd(5)
liste.addEnd(6)
liste.addEnd(7)
liste.deleteSelectedValue(2)
liste.print()








print("Head: " + str(liste.head.data))
print("Tail: " + str(liste.tail.data))
print("Prev Tail: " + str(liste.tail.prev.data))
