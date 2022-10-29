"""Write a python script which takes a three digit number from the user and displays
only its middle digit"""

num_1=int(input("Enter three digit number:"))
if 999>=num_1>=100:
    twodigit=int(num_1/10)
    middledigit=int(twodigit%10)
    print("middle digit is:",middledigit)
else:
    print("invalid number is entered")