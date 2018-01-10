list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num=int(input("Enter the number to be found in list").strip())
new_list=[]
for i in range(len(list)):
    if num>list[i]:
        new_list.append(list[i])
print(new_list)


