#!/usr/bin/env python
#coding:utf-8
import random
import time

def generate_random_int_list(element_num):
    list = []
    for i in range(element_num):
        #while True:
        #    x = random.randint(0, element_num)
        #    if x not in list:
        #        break
        x = random.randint(0, element_num)
        list.append(x)

    return list

def insertion_sort(input_list):
    sorted_list = []
    sorted_list.append(input_list[0])
    input_list.pop(0)

    for insert_elem in input_list:
        if insert_elem < sorted_list[0]:
            sorted_list.insert(0, insert_elem)

        elif insert_elem > sorted_list[len(sorted_list)-1]:
            sorted_list.append(insert_elem)

        else:
            for i in range(len(sorted_list)-1):
                if insert_elem < sorted_list[i+1]:
                    sorted_list.insert(i+1, insert_elem)
                    break

        #print sorted_list

    return sorted_list


def main():
    element_num = 20
    random_list = generate_random_int_list(element_num)
    print random_list
    insertion_sort(random_list)



if __name__ == "__main__":
    main()