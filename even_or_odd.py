num=int(input("Enter number to be checked").strip())
check=int(input("Enter number").strip())
if num%check==0:
    print("Number is divisible")
else:
    print("Number is not divisible")