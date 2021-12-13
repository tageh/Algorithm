#!/usr/bin/ pyhton3

list1 = [1,2,4,5,6]
list2 = [1,2,4,5,6]

def compareList(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    if len1 == len2:
        for i in range(len1):
            if list1[i] == list2[i]:
                print("Alike")
            else:
                print("Not alike")
    else:
        print("List not same length")


compareList(list1, list2)
