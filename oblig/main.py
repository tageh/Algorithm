from oblig import LinkedList

showInfo()

while True:
    select = input()

    switch(select):
        case 1:
            list.deleteFirst()
            break
        case 2:
            value = input("What value would you like to add?")
            list.addEndNode(value)
            break
        case 3:
            list.deleteLast()
            break
        case 4:
            value = input("What value would you like to delete?")
            list.deleteSelectedValue(value)
            break
        case 5:
            valueAdd = input("What value would you like to add")
            valueWhere = input("Wich number do you want the value after?")
            liste.addItemAfterValue(valueWhere, valueAdd)
            break
        case 6:
            valueAdd = input("What value would you like to add")
            valueWhere = input("Wich number do you want the value before?")
            list.addItemBeforeValue(valueWhere, valueAdd)
            break
        case 7:
            list.printLength()
            break
        case 8:
            liste.countNumberOfOccurrences()
            break
        case 9:
            list.print()
            break
        case 10:
            list.deleteList()
            break
        default:
            print("Enter a valid value")


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
