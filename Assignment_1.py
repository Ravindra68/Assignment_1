
#Printing output using Format Specifier

name=input("Enter the name : ")
age=int(input("Enter the age : "))
city=input("Enter city : ")
print("Hello %s your age is %i and you stay at %s"%(name,age,city))



#Printing output using Fstring

name=input("Enter your name : ")
age=int(input("Enter your age : "))
print (f"Hello {name} your age is {age}")


#Printing output using format method

name=input("Enter your name : ")
age=int(input("Enter your age : "))
print ("Hello your name is {} and your age is {}".format(name,age))


#To check the data type

a="Ram"
print ("The data type of Ram is",type(a))
b=38
print ("The data type of 38 is",type(b))
c=17.99
print ("The data type of 17.99 is",type(c))
d=True
print ("The data type of True is",type (d))
e=12+42j
print ("The data type of 12+42j is",type(e))

#Extracting some part of string

city="Bengaluru"
print (city[3:7])

#Slicing of a string

city ="Bengaluru"
print (city[0:7:2])
