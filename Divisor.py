num=int(input("Enter a number ").strip())
list=range(1,num)
new_list=[]
for i in range(len(list)):
    if num%list[i]==0:
        new_list.append(list[i])
print(new_list)
