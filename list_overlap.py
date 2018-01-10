list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result_list=[]
#get common elements from 2 lists
for element in list2:
    if element in list1:
        result_list.append(element)

print(result_list)