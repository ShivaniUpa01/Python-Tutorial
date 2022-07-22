# Python tuple
print("Python Tuples", "\n")

# Create Tuples
print("1. Create Tuples")
create_tuple = ()
print("Empty Tuples : ",create_tuple)
create_tuple = ("a","is", "one","of","the","vowels")
print("string in tuple : ", create_tuple)
tuple_list = [1,2,3,4,5,6]
print("Tuples using list : ",tuple(tuple_list))
tuples_1 = tuple('who are you')
print("Tuple with the usr of function : ",tuples_1,"\n")

#Creating a tuple with Mixed Datatypes
print("2. Creating Tuples")
crt_tuple = ('Welcome', 1,'hello', 3.5)
print("tuple with Mixed : ", crt_tuple, type(crt_tuple))
tup1 = (0,1,2,3,4)
tup2 = ("This", "is", "a", "number", "list")
print("Tuples with nested tuple : ", tup1 + tup2)
print(" Multiply the tuple : ", tup1 *3, "\n")

#Accessing the tuple
print("3. Accessing Tuples")
tup = tuple("shivani")
print("original Tuple : ", tup)
print("Accessing tuples with index : ", tup[4])
a,b,c,d,e,f,g = tup
print("value after unpacking : ", a, b ,c)

#Concatenation of Tuple
print("4. Concatenation of Tuples")
con_tup1 = (1,2,3,4)
con_tup2 = ("number", " in", "sequence")
print("concatenation of tuple : ", con_tup1 + con_tup2,"\n")

# Slicing of Tuples
print("5. Slicing of Tuples")
sli_tup = (1,2,3,4,5,6,7,8,9,0)
print("Slicing from starting : ", sli_tup[:5])
print("Slicing till end : ", sli_tup[4:])
print("Slicing in specific range : ", sli_tup[2:7])
print("Slicing's reverse : ", sli_tup[:-3],"\n")

#Deleting a Tuples
print("6. Deleting a Tuples")
del_tup = (1,2,3,4,5,6,7,8,9,0)
print("Original Tuples : ",del_tup)
#del del_tup
print(" Deleting Tuples : ", del_tup,"\n")

#Built_in method in Tuples
print("6. Built_in Method a Tuples")
builtin_mtup = (1,2,3,4,5,6,0,1,0,5,7,2,8,9,0)
print("Original Tuples : ", builtin_mtup)
print("Index of tuples : ", builtin_mtup.index(9))
print("Count of tuples : ", builtin_mtup.count(0),"\n")

#Built-in function
print("Built-in Function")
builtin_ftup = (1,2,3,8,9,1,3,6,7,8,2,6,4,5,9,5,4,5,6,0,1,0,5,7,2,8,9,0)
print("Original Tuples : ", builtin_ftup)
print("All Function : ",all(builtin_ftup))
print("Any Function : ",any(builtin_ftup))
print("Length Function : ",len(builtin_ftup))
t1 = enumerate(builtin_ftup)
print("Enumerate function : ", type(t1),list(t1))
print("Maximum Function : ",max(builtin_ftup))
print("Minimum Function : ",min(builtin_ftup))
print("Add Function : ", sum(builtin_ftup))
print("Sort Function : ", sorted(builtin_ftup))
string = tuple("Tuple is ended here")
print("Tuple Function : ",tuple(string),"\n", sorted(string))
