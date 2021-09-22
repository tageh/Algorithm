import oblig

list = oblig.LinkedList()


def showInfo():
    print("1: Delete an item first in the list")
    print("2: Add an item to the end of the list")
    print("3: Delete an item at the end of the list")
    print("4: Delete an item with the specified value from the list")
    print("5: Add an item after an item with the specified value")
    print("6: Add an item in front of an item with the specified value")
    print("7: Print the length of the list")
    print("8: Count the number of occurrences of element with given value in the list, this number is printed")
    print("9: Print the entire list")
    print("10: Delete the entire list. How many items were deleted is printed")

showInfo()
while True:
    select = input()

    if select == '1':
       list.deleteFirstNode()
       print("First value deleted")
    elif select == '2':
        value = input("What value would you like to add? ")
        list.addEndNode(value)
        print("Value '" + value +"' added")
    elif select == '3':
        list.deleteLastNode()
        print("Last value deleted")
    elif select == '4':
        value = input("What value would you like to delete? ")
        list.deleteSelectedValue(value)
        print("value '" + value + "deleted")
    elif select == '5':
        valueAdd = input("What value would you like to add? ")
        valueWhere = input("Wich number do you want the value after? ")
        list.addItemAfterValue(valueWhere, valueAdd)
        print("value '" + valueAdd + "' added after " +valueWhere)
    elif select == '6':
        valueAdd = input("What value would you like to add? ")
        valueWhere = input("Wich number do you want the value before? ")
        list.addItemBeforeValue(valueWhere, valueAdd)
        print("value '" + valueAdd + "' added before " +valueWhere)
    elif select == '7':
        print("Length of list is: " +str(list.printLength()))
    elif select == '8':
        value = input("Which number do you want to see the occurrences of? ")
        print("The value '" + value + "' occurrences " +str(list.countNumberOfOccurrences(value)) + " times")
    elif select == '9':
        print("Printing list:")
        list.print()
    elif select == '10':
        list.deleteList()
        print("List deleted")
    elif select == '0':
        print("Exit program")
        break
    else:
        print("Enter a valid number!!!!")
