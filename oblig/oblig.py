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



    #Task 9
    def print(self):
        current = self.head
        if current is None:
            print("Empty list")
            return

        while current is not None:
            print(current.data)
            current = current.next
            



