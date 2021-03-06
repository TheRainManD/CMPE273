import asyncio
import uvloop
import sys
import math
import numpy as np
from typing import List 

def file_read(path):
    lst = []
    with open(path) as f:
        for line in f:
            lst.append(int(line.rstrip('\n')))
    return lst

def merge_sort(unsorted_lst):
    if len(list(unsorted_lst)) > 1:
        mid = len(unsorted_lst) // 2
        left = unsorted_lst[:mid]
        right = unsorted_lst[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                #print(left[i] + "<" + right[j])
                unsorted_lst[k] = left[i]
                i += 1
            else:
                unsorted_lst[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            unsorted_lst[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            unsorted_lst[k] = right[j]
            j += 1
            k += 1
    return unsorted_lst

class MinHeapNode: 
    async def create(self, num, input_index, next_index): 
        self.num = num 
        self.input_index = input_index         
        self.next_index = next_index
        return self
  
class MinHeap: 
    async def create(self, lst, size):
        self = MinHeap()
        self.heap_size = size 
        self.node = lst 
        i = (self.heap_size - 1) // 2
        while i >= 0: 
            self.min_heapify(i) 
            i -= 1
        return self
      
    async def get_min(self): 
        if self.heap_size <= 0: 
            return None
        else:
            return self.node[0]

    async def replace_min(self, root): 
        self.node[0] = root 
        self.min_heapify(0) 

    async def min_heapify(self, i): 
        left = left_node(i) 
        right = right_node(i) 
        smallest = i 
        if left < self.heap_size and self.node[left].num < self.node[i].num:
            smallest = left 
        if right < self.heap_size and self.node[right].num < self.node[smallest].num:
            smallest = right
        if smallest != i: 
            swap(self.node, i, smallest) 
            self.min_heapify(smallest) 

  
  
def left_node(i):
    node_index = 2 * i
    return node_index 
  
  
def right_node(i):
    node_index = 2 * i + 1
    return node_index
  
  
def swap(node, i, j): 
    temp = node[i] 
    node[i] = node[j] 
    node[j] = temp 
  
  
async def merge_k_sorted_lists(lst, size):
    sorted_lst = []
    heap = [] 
    result_size = 0
    for i in range(len(lst)): 
        node = MinHeapNode()
        node.create(lst[i][0], i, 1)
        #await asyncio.gather(node.create(lst[i][0], i, 1))
        heap.append(node) 
        result_size += len(lst[i])
  
    min_heap = MinHeap()
    min_heap.create(heap, size) 
    result = [0]*result_size 
    for i in range(result_size): 
        root = min_heap.get_min()
        result[i] = root.num 
        if root.next_index < len(lst[root.input_index]): 
            root.num = lst[root.input_index][root.next_index] 
            root.next_index += 1
        else: 
            root.num = sys.maxsize 
        min_heap.replace_min(root)
         
    for x in result: 
        sorted_lst.append(x)
        
    return sorted_lst


async def main():
    '''
    path_1 = "/Users/mac/Documents/Python3.8.1/Lab1/input/unsorted_1.txt"
    path_2 = "/Users/mac/Documents/Python3.8.1/Lab1/input/unsorted_2.txt"
    path_3 = "/Users/mac/Documents/Python3.8.1/Lab1/input/unsorted_3.txt"
    path_4 = "/Users/mac/Documents/Python3.8.1/Lab1/input/unsorted_4.txt"
    path_5 = "/Users/mac/Documents/Python3.8.1/Lab1/input/unsorted_5.txt"
    path_6 = "/Users/mac/Documents/Python3.8.1/Lab1/input/unsorted_6.txt"
    path_7 = "/Users/mac/Documents/Python3.8.1/Lab1/input/unsorted_7.txt"
    path_8 = "/Users/mac/Documents/Python3.8.1/Lab1/input/unsorted_8.txt"
    path_9 = "/Users/mac/Documents/Python3.8.1/Lab1/input/unsorted_9.txt"
    path_10 = "/Users/mac/Documents/Python3.8.1/Lab1/input/unsorted_10.txt"

    list_1 = file_read(path_1)
    merge_sort(list_1)
    list_2 = file_read(path_2)
    merge_sort(list_2)
    list_3 = file_read(path_3)
    merge_sort(list_3)
    list_4 = file_read(path_4)
    merge_sort(list_4)
    list_5 = file_read(path_5)
    merge_sort(list_5)
    list_6 = file_read(path_6)
    merge_sort(list_6)
    list_7 = file_read(path_7)
    merge_sort(list_7)
    list_8 = file_read(path_8)
    merge_sort(list_8)
    list_9 = file_read(path_9)
    merge_sort(list_9)
    list_10 = file_read(path_10)
    merge_sort(list_10)


    matrix = np.row_stack((list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9, list_10))
'''
    #print(matrix)
    #print(matrix[0][1])
    #print(len(matrix))
    sorted_lst = merge_k_sorted_lists(matrix, len(matrix))
    await asyncio.gather(sorted_lst)


if __name__ == "__main__":
    path_1 = "/Users/mac/Documents/Python3.8.1/Lab1/input/unsorted_1.txt"
    path_2 = "/Users/mac/Documents/Python3.8.1/Lab1/input/unsorted_2.txt"
    path_3 = "/Users/mac/Documents/Python3.8.1/Lab1/input/unsorted_3.txt"
    path_4 = "/Users/mac/Documents/Python3.8.1/Lab1/input/unsorted_4.txt"
    path_5 = "/Users/mac/Documents/Python3.8.1/Lab1/input/unsorted_5.txt"
    path_6 = "/Users/mac/Documents/Python3.8.1/Lab1/input/unsorted_6.txt"
    path_7 = "/Users/mac/Documents/Python3.8.1/Lab1/input/unsorted_7.txt"
    path_8 = "/Users/mac/Documents/Python3.8.1/Lab1/input/unsorted_8.txt"
    path_9 = "/Users/mac/Documents/Python3.8.1/Lab1/input/unsorted_9.txt"
    path_10 = "/Users/mac/Documents/Python3.8.1/Lab1/input/unsorted_10.txt"

    list_1 = file_read(path_1)
    merge_sort(list_1)
    list_2 = file_read(path_2)
    merge_sort(list_2)
    list_3 = file_read(path_3)
    merge_sort(list_3)
    list_4 = file_read(path_4)
    merge_sort(list_4)
    list_5 = file_read(path_5)
    merge_sort(list_5)
    list_6 = file_read(path_6)
    merge_sort(list_6)
    list_7 = file_read(path_7)
    merge_sort(list_7)
    list_8 = file_read(path_8)
    merge_sort(list_8)
    list_9 = file_read(path_9)
    merge_sort(list_9)
    list_10 = file_read(path_10)
    merge_sort(list_10)
    matrix = np.row_stack((list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9, list_10))
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
    path = "/Users/mac/Documents/Python3.8.1/Lab1"
    
    with open('sorted_list.txt', 'w') as file:
        for item in sorted_lst:
            file.write("%s \n" % str(item))
        file.close()

#asyncio.run(main())
