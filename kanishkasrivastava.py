def merge_sort(list1, left_index, right_index):  
    if left_index >= right_index:  
        return  
  
    middle = (left_index + right_index)//2  
    merge_sort(list1, left_index, middle)  
    merge_sort(list1, middle + 1, right_index)  
    merge(list1, left_index, right_index, middle)  
def merge(list1, left_index, right_index, middle):  
    left_sublist = list1[left_index:middle + 1]  
    right_sublist = list1[middle+1:right_index+1]  
    # track of where we are in each list1  
    left_sublist_index = 0  
    right_sublist_index = 0  
    sorted_index = left_index  
  
    while left_sublist_index < len(left_sublist) and right_sublist_index < len(right_sublist):  
        if left_sublist[left_sublist_index] <= right_sublist[right_sublist_index]:  
            list1[sorted_index] = left_sublist[left_sublist_index]  
            left_sublist_index = left_sublist_index + 1  
        else:  
            list1[sorted_index] = right_sublist[right_sublist_index]  
            right_sublist_index = right_sublist_index + 1  
  
  
        sorted_index = sorted_index + 1  
  
       
    while left_sublist_index < len(left_sublist):  
        list1[sorted_index] = left_sublist[left_sublist_index]  
        left_sublist_index = left_sublist_index + 1  
        sorted_index = sorted_index + 1  
  
    while right_sublist_index < len(right_sublist):  
        list1[sorted_index] = right_sublist[right_sublist_index]  
        right_sublist_index = right_sublist_index + 1  
        sorted_index = sorted_index + 1  
  
list1 = [4, 6, 2, 3, 5, 14, 5, 23, 10, 1, 7, 7, 4]  
merge_sort(list1, 0, len(list1) -1)  
print(list1)  


