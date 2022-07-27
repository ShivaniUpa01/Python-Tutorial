#For Loop
print("For Loop in Python \n")

#for Syntax with simple Example
print("1. For Loop simple Example")
a = [1,2,3,4,5,6,7,8,9,10]
for i in a:
    print(i)
print("This is a simple For Loop \n")

# Using For Loop in Python Dictionary
print("2. Using For Loop on Dictionary")
d = dict()
d[123] = 'abc'
d[456] = 'def'
for i in d : 
    print("% d % s" % (i, d[i]))
print("This is a Eimple Example of using for loop in Dictionary \n")

# Using For Loops in Python String 
print("3. String Using For Loop")
s = " Hello, I am here to learn"
for i in s:
    print(i)
print("String Accessing by For Loop \n")

#Loop Control Statement
#Continue Statement in Python
print("4. Continue Statement loop control statement in python")
for i in "hello world" : 
    if i == 'o' or i == 'l':
        continue
    print("The word is : ", i)
print("This is a Continue  Loop Control Statement \n")

#Break Loop Control Statement
print("5. Break Statement in Python")
for letter in "break statement":
    if letter == 'e' or letter == 'a':
        break 
print("The Current Letter is : ", letter, "\n")

#Pass Loop Control Statement 
print("6. Pass Loop Control Statement")
for letter in "pass statement":
    pass 
print("letter in pass statement : ", letter, "\n")

#Range() Function in For Loop
print("7. Range() function in For loop")
for i in range(10):
    print(i, end=" ")
    
add = 0
for i in range(1, 10):
    add += i
print("Add the number with the help of range function : ", add, "\n")

# Python program to demonstrate
# for-else loop
for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("No Break\n")
