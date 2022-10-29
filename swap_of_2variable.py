#Write a python script to swap data of two variables.
num_1=int(input("Enter the first value:"))
num_2=int(input("Enter the second value:"))
num_1,num_2=(num_2,num_1)
print("value of first after swapping:",num_1)
print("value of second after swapping:",num_2)