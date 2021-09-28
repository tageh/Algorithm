#!/usr/bin/env python3
from random import randrange
import LinkedList
from Node import Node


linked_list = LinkedList.LinkedList(Node)
options = linked_list.get_option_list()

for i, option in enumerate(options):
    print("{}: {}".format(i+1, option))

while True:
    select = input("~ ")  

    if select == '1':
       print("The first node with the value {} was deleted".format(linked_list.delete_first_node().data))
    elif select == '2':
        value = input("What value would you like to add?")
        linked_list.add_node_to_end(value)
        print("Value '" + value +"' added")
    elif select == '3':
        print("Last value with the value {} was deleted".format(linked_list.delete_last_node().data))
    elif select == '4':
        value = input("What value would you like to delete? ")
        print("'{}' was deleted '{}' times".format(value, linked_list.delete_nodes_with_value(value)))
    elif select == '5':
        valueAdd = input("What value would you like to add? ")
        valueWhere = input("Which number do you want the value after? ")
        linked_list.add_node_after_value(valueWhere, valueAdd)
        print("value '" + valueAdd + "' added after " +valueWhere)
    elif select == '6':
        valueAdd = input("What value would you like to add? ")
        valueWhere = input("Wich number do you want the value before? ")
        linked_list.add_node_before_value(valueWhere, valueAdd)
        print("value '" + valueAdd + "' added before " +valueWhere)
    elif select == '7':
        print("Length of list is: " +str(linked_list.listLength()))
    elif select == '8':
        value = input("Which number do you want to see the occurrences of? ")
        print("The value '" + value + "' occurrences " +str(linked_list.get_occourences(value)) + " times")
    elif select == '9':
        print("Entire list:")
        # Get length of list, then loop that many times
        nodes = linked_list.get_list()
        for i, node in enumerate(nodes):
            print("{}:   {}".format(i, node))
    elif select == '9b':
        print("Printing list backwards:")
        nodes = linked_list.get_list(True)
        for node in nodes:
            print(node)
    
    elif select == '10':
        linked_list.delete_list()
        print("List deleted")
    elif select == '0':
        print("Exit program")
        break
    elif select == '11':
        amount = int(input("How many nodes do you want?: "))
        print("Select the range you want the numbers to be within")
        lower = int(input("From(inclusive): "))
        upper = int(input("To(not inclusive): "))
        for node in range(amount):
            linked_list.add_node_to_end(str(randrange(lower, upper)))
    else:
        print("Enter a valid number!")
