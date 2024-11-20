# Write a Python program to count the number 4 in a given list.

list_a=[1,4,6,7,4]
count=0
for i in list_a:
    if i == 4:
        count+=1

print("The number of 4 in a given list is",count)