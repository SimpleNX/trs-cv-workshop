import numpy
print(numpy.__version__)


print("Hello World")

#num = (int)(input("Enter a number :"))
#name = input("Enter a name:")
#print("num :", num, "Name :", name)

val = 5.0
print(val, type(val))

a=5
b=6

mod = b%a
add = a+b
sub = b-a
prod = a*b
ex = a**b

print("{} + {} = {}".format(a,b,add))

t = True
f = False
print(t^f)

#String Operations

String = 'ASTRING'

s1 = slice(-1,-12,-2)
print(String[s1])
print(String[-1:2:-1])
String.replace("S", "A")
print(String)
#.strip function

#List

List =[] #Can contain data of various types
List.append("Heo")
List.pop()
List.insert(0,"popped")
#Slice also works here.

#Dictionary
#Works as a map
#Dictionary functions : adding key values and remove instances of key by del().

#Set Basic Working as C++ STL Set
var = {"Winter", "School", "Robotics"}#Sorts automatically
#add values to a set.
var2 = {"Winter", "TRS", "CV"}
print(var.union(var2))
print(var.intersection(var2))

#Tuple
#Add Elements, cannot change element, Immutable
#Tuple Unpacking a,b,.....,n = Tuple of n elements

#Control Flow

age = 25
if(age>18):
    if(age>60):
        print("CVCNW")
    else :
        print("CVCW")
else:
    print("CNVCNW")

#For-Loop & While Loop
#for <var> in <container>:
#for <var> in range (a,b,c):
#print(<var>, end = " ") without end statement it defaults with newline character.

for i in range(1,7,1):
    for j in range(1,i+1,1):
        print(j, end="* ")
    print("\n")

#Functions.
def here(a):#Parameters
    print(a, "Here")
for i in range(1,5,2):
    here(i)#Arguments
#Types of Arguments:
    #Positional arguments, Default arguments, Keyword arguments.

#Object Oriented Programming:
#Class is a user defined data structure which is a blueprint from which objects can be created and used.
#Objects are instances of a class, it inherits all properties of the class.
#self is an ref to the current instance of the class.
#__init__, constructor funtion used for initiliasing
