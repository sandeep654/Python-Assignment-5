"""Write a python script which takes a three digit number from the user and displays
only its last digit"""

num_1=int(input("Enter three digit number:"))
if 999>=num_1>=100:
    lastdigit=int(num_1%10)
    print("last digit is:",lastdigit)
else:
    print("invalid number is entered")