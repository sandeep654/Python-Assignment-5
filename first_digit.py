"""Write a python script which takes a three digit number from the user and displays
only its first digit"""

num_1=int(input("Enter three digit number:"))
if 999>=num_1>=100:
    firstdigit=int(num_1/100)
    print("first digit is:",firstdigit)
else:
    print("invalid number is entered")