import random
import LinkedList

linkedList = oblig.LinkedList()
options = linkedList.getOptionList()
for i, option in enumerate(options):
    print("{}: {}".format(i+1, option))

while True:
    select = input()

    if select == '1':
       linkedList.deleteFirstNode()
       print("First value deleted")
    elif select == '2':
        value = input("What value would you like to add? ")
        linkedList.addEndNode(value)
        print("Value '" + value +"' added")
    elif select == '3':
        linkedList.deleteLastNode()
        print("Last value deleted")
    elif select == '4':
        value = input("What value would you like to delete? ")
        linkedList.deleteNodesWithValue(value)
        print("value '" + value + "deleted")
    elif select == '5':
        valueAdd = input("What value would you like to add? ")
        valueWhere = input("Which number do you want the value after? ")
        linkedList.addNodeBeforeValue(valueWhere, valueAdd)
        print("value '" + valueAdd + "' added after " +valueWhere)
    elif select == '6':
        valueAdd = input("What value would you like to add? ")
        valueWhere = input("Wich number do you want the value before? ")
        linkedList.addNodeAfterValue(valueWhere, valueAdd)
        print("value '" + valueAdd + "' added before " +valueWhere)
    elif select == '7':
        print("Length of list is: " +str(linkedList.listLength()))
    elif select == '8':
        value = input("Which number do you want to see the occurrences of? ")
        print("The value '" + value + "' occurrences " +str(linkedList.countOccourenes(value)) + " times")
    elif select == '9':
        print("Printing list:")
        linkedList.printList()
    elif select == '9b':
        print("Printing list backwards:")
        linkedList.printList(True)
    elif select == '10':
        linkedList.deleteList()
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
            linkedList.addEndNode(random.randrange(lower, upper))
    else:
        print("Enter a valid number!!!!")
