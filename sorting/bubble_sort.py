#!/usr/bin/env python
#coding:utf-8
import random
import time

def generate_random_int_list(element_num):
    list = []
    for i in range(element_num):
        x = random.randint(0, element_num)
        list.append(x)

    return list

def bubble_sort(input_list):
    sorted_list = input_list
    while True:
        if check_sorted(sorted_list) == True:
            break

        else:
            for i in range(0, len(sorted_list)-1):
                if sorted_list[i] > sorted_list[i+1]:
                    tmp = sorted_list[i]
                    sorted_list[i] = sorted_list[i+1]
                    sorted_list[i+1] = tmp

        #print sorted_list

    return sorted_list

def check_sorted(input_list):
    for i in range(0, len(input_list)-1):
        if input_list[i] > input_list[i+1]:
            return False

    return True

def main():
    element_num = 1000
    random_list = generate_random_int_list(element_num)

    start_time = time.time()
    bubble_sort(random_list)
    print str(time.time()-start_time)

if __name__ == "__main__":
    main()

