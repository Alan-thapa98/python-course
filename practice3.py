# takinf the input fron the user 
print("Enter the number of list list one by one")
size=int(input("Enter the size of list\n"))
# inicilazation the blank list form the user 
mylist=[]
for i in range(size):
    mylist.append(int(input("Enter the list element\n")))
    print(f"your list is {mylist}\n")

# these is the first reverse method 
reverse1=mylist[:]
reverse1.reverse()
print(f"your list {mylist} is reversed {reverse1}")

# these is the second reversed method
reverse2=mylist[::-1]
print(f"your list second  {mylist} is reversed {reverse2}")
# print(f"your list {mylist} is reversed {mylist[::-1]}")

# these is the thired revrsed methord 
reverse3=mylist
for i in range(len(reverse3)//2):
    reverse3[i],reverse3[len(reverse3)-i -1]=reverse3[len(reverse3)-i -1], reverse3[i]
print(f"Your list thired {mylist} is reversed { reverse3}")

# jest for the sour if the list is same  or not 
if reverse1 and reverse2 == reverse3:
    print("Your all the list are same.")

# ***********************         the end           *********************