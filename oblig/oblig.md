# Obligatory Assignment 1
## Pseudo code
Input: One integer that the user enters

TODO:
1. Create a node class
2. Create a linked list class

class Node:
    data
    next
    prev

class LinkedList:
    head = none
    tail = none

## Task 1 b
**Delete first element in linked list**  
move head to next node, possibly set prev to null

## Task 2
**Add element to the end of the linked list**
Check if head has a node, if not, make head point to new node.
Set new_node.prev to tail, then set tail.next to new node, then tail to new node

## Task 3
**Delete element at the end of the linked list**
Same as 1

## Task 4
Check if head exists, if not return that the number doesn't exist. Traverse through the entire list, check if the given value is equal to the nodes value. If it is, then 

## Task 9
Check if head is not none, then continue traversing, printing out data and going to the next node for each iteration


