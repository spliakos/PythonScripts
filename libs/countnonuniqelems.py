#!/usr/bin/python

numbers = [1, 5, 1, 6, 3, 5, 2, 8]

def countNonUnique(numbers):
    # Write your code here
    countnum = 0
    templist = numbers[:]
    for i in templist:
        if templist.count(i) > 1:
            templist.remove(i)
            countnum = countnum + 1
    

    return countnum


if __name__ == '__main__':
	mycount = countNonUnique(numbers)
	print "%d" %mycount
