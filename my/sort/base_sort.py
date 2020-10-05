#!/usr/bin/python
# -*- coding: UTF-8 -*-
def bubble_sort(array):
    length = len(array)
    isEnd  = None
    tmp    = None
    for i in range(length):
        # 每一轮都去判断
        isEnd = True
        for j in range(length - i - 1):
            # 只要不相等交换，相等值得先后顺序是不变的
            if array[j] > array[j + 1]:
                tmp          = array[j + 1]
                array[j + 1] = array[j]
                array[j]     = tmp
                isEnd        = False
        if isEnd:
            return

def insert_sort(array):
    length          = len(array)
    # 第一个直接当做有序区
    for i in range(1, length):
        j           = i - 1 # 从有序区直接开始
        need_insert = array[i]
        # array[j] > need_insert 为了保证稳定的排序
        while j >= 0 and array[j] > need_insert:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = need_insert

# 找到最小，交换
def select_sort(array): 
    length        = len(array)
    for i in range(length):
        min_val       = float("+inf")
        min_val_index = 0
        for j in range(i, length):
            if array[j] < min_val:
                min_val_index = j
                min_val       = array[j]
        # tmp                  = array[i]
        # array[i]             = array[min_val_index]
        # array[min_val_index] = tmp
        array[i], array[min_val_index] = array[min_val_index], array[i]

if __name__ == "__main__":
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    bubble_sort(array)
    print(array)
    
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    insert_sort(array)
    print(array)
    
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    select_sort(array)
    print(array)