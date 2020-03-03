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

        list.append(x)

    return list

def selecting_sort(input_list):
    list_len = len(input_list)
    sorted_list = []

    while True:
        if len(sorted_list) == list_len:
            break

        else:
            min_value_idx = get_min_value_idx(input_list)
            sorted_list.append(input_list[min_value_idx])
            list.pop(min_value_idx)

        #print sorted_list

    return sorted_list


def get_min_value_idx(input_list):
    min_value_idx = -1
    min_value = 100000000000

    for i, elem in enumerate(input_list):
        if elem < min_value:
            min_value = elem
            min_value_idx = i

    return min_value_idx

def main():
    element_num = 10
    random_list = generate_random_int_list(element_num)

    print random_list
    #selecting_sort(random_list)
    print selecting_sort(random_list)



if __name__ == "__main__":
    main()