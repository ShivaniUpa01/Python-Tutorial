Python List


# Online Python - IDE, Editor, Compiler, Interpreter
test =[]
num_list = [10,20,30,40,50]
str_list = ["suraj", "shivani", "random"]
multi_dim = [["This","list", "is"], ["Multi","dimensional"]]

#Simple Print
print("1#. Simple Print")
print (num_list[2],"\n")

#Finding Last element
print("2#. Last Element of List ")
print (str_list[len(str_list)-1],end="  --*--   ")
print ("Last element ", num_list[-1],"\n")

#Access element from multi dimensional list
print("3#. Access and print Multi-Dimensional of list")
print(multi_dim[0][2], multi_dim[1][1],"\n")

#negative indexing
print("4#. Negative Indexing")
print(multi_dim[0][-2], multi_dim[1][-2] ,end="  --*--   ")
print(num_list[-0],end="  --*--   ")
print(str_list[-3], "\n")

#Get the size of python list
print("5#. Size of List")
print("Number list : ",len(num_list)," String list : ", len(str_list), " Multi Dimensional : ",len(multi_dim), "\n")

#Taking input from the user
print("6#. Take input from user")
string_list = "how are you"
#take_input = input("Enter your name : ", )
take_input = "Enter your name : " + string_list
split_str = take_input.split()
print("this is charater wise list : ",list(take_input))
print("The Split Function split the through space : ", split_str , "\n")

#Put the value inside the empty list 
print("7#. Adding Elements to a Emp[ty list")
empt_list = []
empt_list.append("string")
empt_list.append(2)
empt_list.append(3.55)
print("The Empty list after Append function : ", empt_list, " \n")

#Insert the valuse in desire position
print("8#. Insert function help to insert the value at the desire position ")
insert_list = [1,5,6,7,8,9,3]
print("The Original List  : " , insert_list)
insert_list.insert(4, "a")
insert_list.insert(2, "value")
print("After performing the Insert function : ", insert_list, "\n")

# Extend function 
print("9#. Extend Function is used to add multiple element in list at a same time at the end ")
ext_list = [2,3,6,8,4,9,7]
print("Original List : ", ext_list)
ext_list.extend(["a","e","i",2.3, 5.4, 6.8])
print("Extended List : ", ext_list, "\n")

#Reserve the List Elements
print("10#. Reserve the element of the list")
rsv_list = [1,2,3,4,5,6,7,8,9]
print("Original list : ", rsv_list)
rsv_list.reverse()
print("Reserved List : ", rsv_list,"\n")

#Remove the element from the list
print("11#. Remove the value from the List")
rmv_list = [1,2,3,4,5,6,7,8,9]
print("Original list : ",rmv_list)
rmv_list.remove(5)
print("Remove First elements : " ,rmv_list)
rmv_list.remove(8)
print("Remove Second elements : " ,rmv_list, "\n")

#Pop function use to delete element from end one-by-one
print("12#. Pop Function is used to delete the element")
pop_list = [1,2,3,4,5,6,7,8,9]
print("Original list : ",pop_list)
pop_list.pop()
print("Pop list with empty function : ", pop_list)
pop_list.pop(5)
print("Pop element with specific elements : ", pop_list, "\n")

#Slicing of a list
print("Slicing of a List")
slice_list = [1,2,3,4,5,6,7,8,9]
print("Original list : ",slice_list)
print("Slice element from start to end : ", slice_list[:])
print("Slice element form  starting : ", slice_list[:4])
print("Slice element from specific range : ", slice_list[3:7])
print("Slice elements from specific position till end : " ,slice_list[6: ],)
print("Slice elements in alternative order : ", slice_list[3::2], slice_list[:8:2])
print("Slice elements in reveerse order : ", slice_list[::-1], slice_list[::-2], "\n")

# Negative Indices list Slicing
print("13#. Negative Indices list in slicing function")
slice_list = [1,2,3,4,5,6,7,8,9]
print("Original list : ",slice_list)
print("Slice element from start to end : ", slice_list[:])
print("Slice element form  starting : ", slice_list[:-4])
print("Slice element from specific range : ", slice_list[-7:-3])
print("Slice elements from specific position till end : " ,slice_list[-6: ],)
print("Slice elements in alternative order : ", slice_list[-3::2], slice_list[:-4:2], "\n")

#List Comprehension
print("14#. List Comprehension")
odd_square = [[x ** 2 for x in range(1, 11) if x % 2 == 1], [x ** 2 for x in range(1, 11) if x % 2 == 0]]
print(odd_square,"\n")

#Remaining list Methods
print("15#. Remaining List Method ")
rem_list = [12,15,13,10,5,2,7,8,6,14,11,1,3,9,4,0,5,4,5,8]
print("Original List : ", rem_list)
print("Count Function : ",rem_list.count(5))
print("Copy Function : ", rem_list.copy())
print("Index Function : ", rem_list.index(5))
print("Sort Function : ", rem_list.sort(),rem_list)
print("Clear Function : ", rem_list.clear(), "\n")

#Buit_in Function
import functools
print("16#. Built_in Function")
print("1. Reduce Function import it with \"Functools\"")
import functools
built_in = [12,15,13,10,5,2,7,8,6,14,11,1,3,9,4,0,5,4,5,8]
built_in1 = [12,15,13,10,5,2,7,8,6,14,5,4,5,8]
print("Reduce Function : ",functools.reduce(lambda a,b :a if a > b else b, built_in))
print("2. Sum Operator Import it with \" Operator \" but i am using simple sum function like sum()")
print("Sum Function : ", sum(built_in) ,sum(built_in, 5))
print("3. Ord() used for find Unicode of character")
print(" Ord Function : ",ord("1"))
'''print("4. Cmp() for comparing the two list")
print ("Cmp function : ", end="")
print (cmp(built_in1, built_in))'''
print("4. Max function")
print("Max Function : ", max(built_in))
print("5. Min Function")
print("Min Function : ", min(built_in))
print("6. All Function ")
print("All Function : ",all(built_in))
print("7. Any Function ")
print("Any Function : ",any(built_in))
print("8. Len Function")
print("Len Function : ", len(built_in))
print("9. Enumerate Function")
l1 = enumerate(built_in)
print("Enumerate Function : ",type(l1),list(l1))
"""print("10. Accumulate Function")
print("Accumulate Function : ", accumulate(built_in))"""
print("10. Filter Function")
#Find all the pairs where first > second
l1 = filter(lambda x : True if x[0] > x[1] else False, [[1,2],[2,2], [5,3]])
print("Fliter Function : ", list(l1))
