check_palindrome=input("Enter a string")
length_=len(check_palindrome)
flag=False
if length_%2!=0:
    if check_palindrome[0:(length_//2)+1] == check_palindrome[:(length_//2)-1:-1]:
      flag=True
else:
    if check_palindrome[0:(length_//2)+1] == check_palindrome[:(length_//2)-1:-1]:
       flag=True
if flag:
    print(check_palindrome + " is a palindrome string")
else:
    print(check_palindrome + " is not a palindrome string")
      