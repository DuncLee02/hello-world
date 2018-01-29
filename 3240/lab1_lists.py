# Duncan Lee (ddl9be)
# Lab 101
# lab1_fact.py
# January 22, 2018

def maxmin(list):
    min = list[0]
    max = list[0]
    for item in list:
        if item < min:
            min = item
        if item > max:
            max = item
    return (max, min)


def common_items(list1, list2):
    common = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                contains = False
                for commomItem in common:
                    if commomItem == item1:
                        contains = True
                if contains == False:
                    common.append(item1)
    return common


if __name__ == "__main__":
    listA = [1, 2, 3, 4]
    assert maxmin(listA) == (4, 1), "maxmin not working"

    listB = ['a', 'b', 'g', 'z']
    assert maxmin(listB) == ('z', 'a'), "maxmin not working"

    assert common_items(listA, listB) == [], "common items returning items when none found"

    listC = [2, 4, 7, 8]
    assert common_items(listA, listC) == [2, 4], "common items returning wrong items"

