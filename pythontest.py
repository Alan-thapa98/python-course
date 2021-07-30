
# class Employee():
#   num_of_leves=16

#   def __init__(self,fname,lname,salary,role):
#         self.fname=fname
#         self.lane=lname
#         self.salary=salary
#         self.role=role

#   def printdatiles(self):
#         print(f"My name is {self.fname} {self.fname}. MY salary is {self.salary}.My role is {self.role}.")
        
# alan=Employee("alan","thapa ",1000000, "programmer")
# may=Employee("may","thapa ",1000000, "programmer")
# muskan=Employee("muskan","subadi ",3000, "bank manager")

# alan.printdatiles()
# may.printdatiles()
# muskan.printdatiles()

# # these is  the  functions 
# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)

#  for x in range(6):
#       print(x)
# else:
#   print("Finally finished!")


# these is for the class/objects
# class Person:
#       def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my name is " + abc.name)

# p1 = Person("John", 36)
# p1.myfunc()


# # inharitens 
# class Student(Person):
#       def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# class MyNumbers:
#       def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# formating
# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {} pieces of item number {} for {:.2f} dollars."
# print(myorder.format(quantity, itemno, price))


# for i in range(int(input("please enter the num to count.Count will beganin with 0 to the  num that you have given: \n"))):
#       print(i)




# these is for the set ok 
# set1={1,2,34,5}
# set2={233,32,334,35,1,2,34,5}
# set1.add(22)
# set1.remove(2)
# print(set1)
# print(set1.union({1,2}))
# print(set1.intersection({1,2,24}))
# print(type(set1))

# these is the set of list 
# list1=["alan","may","Muskan","Deepa","Suresh"]
# # for item in list1:
# #       print(list1)
# for item, loyeypop in list1:
#       print(item,"any things ,",loyeypop)


# these is the another proble of the another case
# i=0;
# while True:
#       print(i+1,end=" ")
#       if(i==44):
#             break
#       i=i+1
# while True:
#       if i+1<45:
#             i=i+1
#             continue
#       print(i,end=" ")
#       if (i==44):
#             break
#       i=i+1


# these is for the function of the list these is not working ok 
# def function1(a,b):
#       """these  for the multi lline comment ok """
#       print("hello word ",a+b)
#       function1()
# # print(function1.__doc__)

# def function2(a,b):
#       average=(a+b)/2
#       print(average)
#       return average
# var2=function2(1,2)
# print(var2)


# num1=int(input("Please enter the first number \n"))
# num2=int(input("Please enter the second number \n"))
# try:
#       print("the sum of two number is ",int(num1)+int(num2))
# except Exception as e:
#       print(e)
# print("hello it is me alan ")


# these is  for the file hadaling 

# f=open("one.txt", 'r')
# content=f.read()
# print(content)