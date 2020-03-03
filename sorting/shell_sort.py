#!/usr/bin/env python
#coding:utf-8
import random
import time

def generate_random_int_list(element_num):
    list = []
    for i in range(element_num):
        while True:
            x = random.randint(0, element_num)
            if x not in list:
                break
        #x = random.randint(0, element_num)
        list.append(x)

    return list

def shell_sort(lst):
    print("00:",lst)
    length = len(lst)
    h = 1
    while h < length / 9:
        h = h * 3 + 1

    print "h: ", h
    print "length", length

    while h > 0:
        for i in range(h, length):
            j = i
            while j >= h and lst[j-h] > lst[j]:
                tmp = lst[j]
                lst[j] = lst[j-h]
                lst[j-h] = tmp
                j -= h
            print("{:02}: {}".format(i+1, lst))
        h = int(h / 3)


def main():
    element_num = 10
    random_list = generate_random_int_list(element_num)
    #random_list = [8,2,7,6,9,1,4,3,5]

    print "random " + str(random_list)

    sorted_list = shell_sort(random_list)

    #print "sorted " + str(sorted_list)

if __name__ == "__main__":
    main()