# Variables

#a = 10
a = ''' Hi there
i am grace'''

# Basic function
# Input
'''a = int(input()) # default string
b = int(input())'''
'''a = 5
b = 4
#Print
#print(" Hi ", a+b, end = "") #end = Default \n next line
print("hi","namz",sep = "*")
'''
# operators
'''
+ -> addition
- -> subtraction
* -> Multiplication
/ -> division 5/2 = 2.5
// -> Quotient
% -> Remainder
** -> Exponent 5**2 =25

ternary operator
true_value if <condition> else false_value
print("You can drive") if (age>=18) else print("You cannot drive")

<variable> = true_value if <condition> else false_value

a = 20 if (chocolate = 'Dairy Milk') else 10
'''

# Store -> Similar to array
'''
1) List = []
ex: a = [4, "hi", 3.14] # Change the element(mutable)
index  4->0     hi->1       3.14->2
       4->-3    hi->-2      3.14->-1
       
a[-1] = 22/7

2) Tuple = ()
ex: car = ('audi', 'VW', 'BMW') # immbutable
a[-1] = "ford" -> ERROR

3) Set 
a = {1,2,2,3}
print(a) -> {1,2,3} # No repeitive elements
union intersection difference

4) Dictionary 
key value  // key is unique 
"Name"-> "Namz"
"Friend_Name"->"Namz"
'''

# Condional stats

'''age = int(input())
# Tab space = 4 spaces
if (age>=18):
    print("You can drive")

elif (age < 0):
    print("Age is not possible")

else:
    print("You cannot drive")'''

# looping -> for and while

'''i = 1
while(i <10):
    print(i)
    i += 1'''

# For loop

'''for i in range(0,10, 5): # Last value -1
    # 1 2 3 4 5 6 7 8 9
    print(i)
'''

'''for i in "Hello World":
    print(i, end = "")'''

'''car = ['audi', 'VW', 'BMW']

for i in car:
    for j in i:
        print(j)'''

# Logical operators
# and or

a = 'Hi I am Grace'

if 'Grace' in a:
    print("Hi")
