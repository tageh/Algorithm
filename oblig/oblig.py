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

    def emptyList(self, node):
        if node is None:
            print("List is empty")
            return True
        return False

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

    def addNodeAfterValue(self, val, insVal):
        curr = self.head

        if self.emptyList(curr):
            return
        
        while curr is not None:
            newNode = Node(insVal)
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

    def addNodeBeforeValue(self, val, insVal):
        curr = self.tail

        if self.emptyList(curr):
            return
        
        while curr is not None:
            newNode = Node(insVal)
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

    
    def listLength(self):
        curr = self.head
        count = 0

        if self.emptyList(curr):
            return

        while curr is not None:
            curr = curr.next
            count += 1
        return count

    def countOccourences(self, value):
        curr = self.head
        count = 0
        
        if self.emptyList(curr):
            return
        
        while curr is not None:
            if curr.data == value:
                count += 1

            curr = curr.next
        return count


    def printList(self, backwards = False):
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

                
    def deleteList(self):
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