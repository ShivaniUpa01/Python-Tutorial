#While loop in Python
print("Using Of While Loop in Python \n")

print("1. simple program of while loop")
count = 0
while (count < 3):
    count += 1
    print("This is a simple while loop : ",count)
print("\n")

#python while loop with list
print("2. While Loop With List in Python")
list1 = ['a', 'b', 'c','d','e']
while list1:
    print("Pop item : ",list1.pop())
    print(list1)
print("Accessing list item with using While Loop")

#Single statement while Block
print("3. While Single Statement bLock")
count = 0
while (count < 5): count +=1 ; print("Hello %d " % count)
print("\n")

#Loop Control Statement
print("4. Python while loop with Continue statement")
i = 0
a = "My World is very big"
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        print(a)
        continue
    print("Continue statement with While loop ", a[i])
    i += 1
print("\n")

#Python while loop with break Statement 
print("5. python while loop with break statement ")
i = 0
a = "World is Very Big"
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break 
    
    print("Break Statement with While Loop : ",a[i])
    i += 1
    
#Python while loop with pass statement 
print("6. While loop with pass statement")
a = "World is Very Big"
i = 0
while i < len(a):
        i += 1
        pass
print("While loop with pass statement : ", i)

# While loop with else statement
print("7. While Loop with else")
i = 0
while i < 4:
     i += 1
     print(i)
else:
    print("No Break ")
    
i = 0
while i < 4:
    i += 1 
    print(i)
    break 
else :
    print(" No Break")
    
#Sentinel Controlled Statement
print("Sentinel Controlled Statement")
a = int(input("Enter a number(-1 to quit) : "))
while a != -1:
    a = int(input("Enter a number (-1 to quit) : ")) 
    
print("This is a pack up of While Loop")
