# # Duck Typing
# class VisualStudioCode:
#     def execute(self):
#         print("Compiling")
#         print("Running") 

# class Laptop:

#     def code(self):
#         ide.execute()

# ide=VisualStudioCode()
# lap1=Laptop()
# lap1.code()



#### operator Overloading

# class Student:
#     def __init__(self,m1,m2):
#         self.m1 =m1
#         self.m2=m2

#     def __add__(self,other):
#         m1= self.m1 +other.m1
#         m2= self.m2 + other.m2
#         s3=Student(m1,m2)
#         return s3


# s1= Student(54,20)
# s2= Student(87,64)

# s3= s1+ s2 
# print (s3.m1)



#method overloading and method overriding
#"method overloading"



# class Student:
#     def __init__(self, m1, m2):
#         self.m1 =m1
#         self.m2=m2
#     def sum(self,a,b):
#         s= a+b

#         return s
# s1 = Student(845,254)

# print(s1.sum(10,15))
     



#iteration

# nums =[1,4,5,6,58,9,6]
# it = iter (nums) 
# print (it.__next__())
# print (next(it))

# for i in nums:
#     print (i)



# class topten:
#     def __init__(self):
#         self.num =1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num <=10:
#             val =self.num
#             self.num   +=1
#             return val
#         else:
#             raise StopIteration

# values= topten()
# print (next(values))

# print(values.__next__())
# for i in values:
#     print(i)




# f= open('hello.py','r')
# print(f)