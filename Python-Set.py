# Python Set Funtions
print("Set of Python")
print("1. Create a empty set")
set1 = set()
print("Create Empty set and store its value in a variable  : ", set1)
set1 = {}
print("Empty set : ", set1)
set1 = {1,5,2,3,0,4,5,6,7,5}
print("Create Set with value : ", set1)
set1 = set("aldkofgvmov") 
set2 = set("AKDNOIVAGI")
print("Create set of strings : ",set1 , set2,"\n")

#Adding elements in a set
print("2. Add Method of set")
set1 = set()
print("Original Set : ", set1)
print("Adding the elements in set : ", set1.add(5), set1)
print("Adding the another elements in set : ", set1.add(6), set1)
print("Adding the similar elements(5) in set : ", set1.add(5), set1,"\n" )

#Update element in a set1
print("3. Update Methof of set")
set1 = {4,5,6,(6,7,8),8,9,0}
print("Original Set : ", set1)
print("Update Method : ",set1.update("shivani"), set1,"\n")

#Accessing of set
print("4. Accessing the elemets from the set")
set1 = {1,6,56,5,8,12,452,58,2 }
print("Original Set : ", set1)
print("Accessing set with for loop")
for i in set1 : 
    print(i ,end=" == ")
    
# Remover and Discard Method in set
print("5. Remove and Discrd Function")
set1 = {1,6,56,5,8,12,452,58,2 }
print("Original Set : ", set1)
print("Remove Function : ", set1.remove(56), set1)
print("Dicard Function : ",set1.discard(58), set1)
print("Dicard Function discard 38: ",set1.discard(38), set1, "\n")

# Pop Method in set
print("6. Pop Method")
set1 = {1,6,56,5,8,12,452,58,2}
print("Original Set : ", set1)
print("Pop Method :", set1.pop(), set1, "\n")

#Clear Method in set 
print("7. Clear Method")
set1 = {1,6,56,5,8,12,452,58,2}
print("Original Set : ", set1)
print("Clear Method : ", set1.clear(), set1,"\n")

#Frozenset in set
print("8. Frozenset")
set1 = {1,6,56,5,8,12,452,58,2}
print("Original Set : ", set1)
print("Frozenset : ", frozenset(set1), set1, "\n")

#Typecasting object into set 
print("8. Typecasting Object into set")
list1 = ['a',1,5,4,3,'g','y','b','d',8,9,4]
string1 = "How are you?, world!"
dict1 = {1:"One", 2:"Two", 3:"Three"}
print("List into set : ", set(list1),list1)
print("String into set : ", set(string1),string1)
print("Dictinary into set : ",set(dict1), set(dict1.values()), dict1,"\n")

#Set Method in set 
print("Set Method")
set1 = {'a','ak',"jdoif",1,6,56,89,245,66,34,61,145}
set2 = {'a','cfg','ak',"jdoif",1,6,565,6,8,16,15158,215,89,245,34,61,145}
print("Union Method : ",set1.union(set2),"\n set 1",set1,"\n set 2",set2)
print("Difference Method : ",set1.difference(set2))
print("Difference Update : ",set1.difference_update(set2) ,set1)
