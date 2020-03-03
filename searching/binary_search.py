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
        x = random.randint(0, 100)
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

def binary_search(input_list, target_value):
    target_idx = -1
    left = 0
    right = len(input_list)-1

    while left <= right:
        center_idx = (left+right)/2
        center_value = input_list[center_idx]

        if center_value == target_value:
            target_idx = center_idx
            break

        elif center_value < target_value:
            left = center_idx + 1

        else:
            right = center_idx - 1


    return target_idx


def main():
    random_list = generate_random_int_list(100)
    sorted_list = quick_sort(random_list)

    target_value = 10
    target_idx = binary_search(sorted_list, target_value)
    print sorted_list
    print "target_idx ", target_idx

if __name__ == "__main__":
    main()