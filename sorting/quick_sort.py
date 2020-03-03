#!/usr/bin/env python
#coding:utf-8
import random
import time

def generate_random_int_list(element_num):
    list = []
    for i in range(element_num):
        #while True:
        #    x = random.randint(1, element_num)
        #    if x not in list:
        #        break
        x = random.randint(0, element_num)
        list.append(x)

    return list

def quick_sort(input_list):
    if len(input_list) < 1:
        return input_list

    pivot = input_list[len(input_list)/2]
    left = []
    right = []
    pivots = []

    for elem in input_list:
        if elem == pivot:
            pivots.append(elem)

        elif elem < pivot:
            left.append(elem)

        else:
            right.append(elem)

    return quick_sort(left) + pivots + quick_sort(right)

def main():
    random_list = generate_random_int_list(20)
    print "random_list ", random_list
    print "sorted_list ", quick_sort(random_list)

if __name__ == "__main__":
    main()