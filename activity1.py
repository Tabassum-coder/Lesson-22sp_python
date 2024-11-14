#Write a program to perform the following operations: 
# 1. Create a tuple with different datatypes 
# 2. Create another tuple of integers 
# 3. Create a new tuple by adding 9 to the previous tuple 
# 4. Count the occurrences of an element in the tuple 
# 5. Perform slicing on the tuple

t1=(4,"Hello",True,42.8)
print("Tuple 1 is ",t1)

t2=(2,10,5,3,18)
print("Tuple 2 is ",t2)

t3=t2+(9,)
print("Tuple 3 is ",t3)

t4=(10,4 ,10,5,10,2,10,7,10)
print("Tuple 4 is ",t4)
print("Occurence of 10 in tuple 4 is ",t4.count(10))

print(t4[1:5])