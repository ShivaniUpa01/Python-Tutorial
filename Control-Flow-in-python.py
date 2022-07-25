#python Control Flow
print("1. Control Flow in Python \n")
#Simple If Statement
a = 20 
if (a != 20):
    print("This is a if Control Flow")
print("I am a IF control Flow Outer Statement and its always print \n")

#If-Else Statement
print("2. Simple If-Else Statement")
a = 60
b = 20 
if a < b :
    print("This is a If statement")
    print("Maximum number : ",a)
else: 
    print("This is a Else Statement")
    print("Minimum number : ",b)
print("I am not If Statement and neither Else Statement \n")

# If Else in List Comprehension
print("3. If-Else in List Comprehension")
def digitalSum(n):
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum

List = [367, 111, 562, 945, 6726, 873]
newList = [digitalSum(i) for i in List if i & 1]
print(newList)

#Nested_if Statement
print("4. Nested-If Statement")
i = 900
if i < 100:
    if i < 80:
        if i < 60:
            if i < 40:
                if i < 20:
                    print("Nested If is less than 20 : ", i)
                print("Nested If is less than 40 : ", i)
            print("Nested If is less than 60 : ", i)
        print("Nested If is less than 80 : ", i)
    print("Nested If is less than 100 : ", i)
else:
    print("Nested Else is Greater than 100 : ", i)
print("This is a Nested If-Else End here \n")

# If-elif-else Control Flow
print("5. If-elif-else Control Flow")
i = 100
if i == 10 :
    print("Print If Statement : ",i)
elif i == 20:
    print("Print first elif Statement : ",i)
elif i == 30:
    print("Print second elif Statement : ",i)
elif i == 40:
    print("Print third elif Statement : ",i)
elif i == 50 : 
    print("Print fifth elif Statement : ",i)
else :
    print("This is a Else Statement : ", i)
print("Here is the  If-elif-else Control Flow end \n")

#Shorthand if statement 
print("6. Short Hand If Statement")
i = 15
if i <= 15: print("This is a Short hand if Statement : ", i)

#Short Hand If-Else Statement
print("7. Short Hand If-Else Statement")
i = 10
print("This is a shorthand, the \"IF\" Statement is True ", i) if i < 15 else print("This is a shorthand, the \"ELSE\"  Statement is True ", i, "\n")
print("This is a shorthand, the \"IF\" Statement is True ", i) if i > 15 else print("This is a shorthand, the \"ELSE\" Statement is True ", i, "\n\n")


print("WE PACK UP THE CONTROL FLOW IN PYTHON")
