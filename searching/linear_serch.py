#!/usr/bin/env python
#coding:utf-8
import random
import time

def linear_search(input_list, target):
    target_idxs = []
    for i, elem in enumerate(input_list):
        if elem == target:
            target_idxs.append(i)

    return target_idxs

def generate_random_int_list(element_num):
    list = []
    for i in range(element_num):
        x = random.randint(0, element_num)
        list.append(x)

    return list

def main():
    element_num = 10000000
    list = generate_random_int_list(element_num)

    target_elem = random.randint(0, element_num)

    print "target_elem ", target_elem
    target_idxs = linear_search(list, target_elem)

    if len(target_idxs) == 0:
        print str(target_elem) + " is not in list."

    else:
        print str(target_elem) + " is at " + str(target_idxs)



if __name__ == "__main__":
    main()