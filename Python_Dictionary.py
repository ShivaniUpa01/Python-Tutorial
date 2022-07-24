#Python Dictionary
print("Dictionary in Python \n")

#Creating Dictionary
print("1. Creating Dictionary")
Dict1 = {1:"shivani",2: 2549, 'a':35.2,'b':369, 2.1: "learn", 3.4 : 365}
Dict2 = {'b': 123 , 'a':[1,2,3,4,5,6],1:['a','b','c','d']}
print("Dictionary 1 : ", Dict1)
print("Dictionary 2 : ", Dict2)
dict1 = {}
print("Empty Dictionary : ",dict1)
dict1 = dict({1:"shivani",2: 2549, 'a':35.2,'b':369, 2.1: "learn", 3.4 : 365})
print("Create Dictionary with dict() method : ", dict1, "\n")

#Nested Dictionary
print("2. Nested Dictionary")
dict1 = {1 : "Hello", 2 : "Hi",3:{'a':"Welcome", 'b':"To", 'c' : "My World!"}}
print("Nested Dictionary : ", dict1,"\n")

#Adding elements to a Dictionary
print("3. Adding elements to a dictionary")
dict1 ={}
print("Original dictionary : ", dict1)
dict1[1] = 32
dict1[2] = 52.5
dict1[3] = "hello"
print("Adding simple elements : ",dict1)
dict1['Value'] = ['hello', 'hi', 'Welcome',1,3,56]
print("Adding bunch of elements : ", dict1)
dict1[4] = {}
dict1[5] = {"Nested" : {1 : "one", 2 : "Two", 3 : "Three"}}
print("Adding empty elements : ",dict1,"\n")

#Accessing elements from the dictionary
print("4. Accessing elements from the dictionary")
Dict = {1: 32, 2: 52.5, 3: 'hello', 'Value': ['hello', 'hi', 'Welcome', 1, 3, 56], 4: {}, 5: {'Nested': {1: 'one', 2: 'Two', 3: 'Three'}}}
print("Original Dictionary : ",Dict)
print("Accessing elements :", Dict[5],Dict[3],"\n")

#Get() Method from Dictionary
print("5. Get() Method from Dictionary")
Dict = {1: 32, 2: 52.5, 3: 'hello', 'Value': ['hello', 'hi', 'Welcome', 1, 3, 56], 4: {}, 5: {'Nested': {1: 'one', 2: 'Two', 3: 'Three'}}}
print("Original Dictionary : ",Dict)
print("Get() Method from Dictionary : ",Dict.get(5)["Nested"])
print("Accesing Nested Dictionary : ", Dict, Dict[5],Dict[5]["Nested"],Dict[5]["Nested"][3], "\n")

#Dictionary Method
print("6. Dictionary Method")
Dict = {1: 32, 2: 52.5, 3: 'hello', 'Value': ['hello', 'hi', 'Welcome', 1, 3, 56], 4: {}, 5: {'Nested': {1: 'one', 2: 'Two', 3: 'Three'}}}
print("Original Dictionary : ",Dict)
Dict1 = Dict.copy()
print("Copy() Method : ",Dict1)
print("Clear() Method : ", Dict1.clear(),Dict1)
print("Items() Method : ",Dict.items())
print("Keys() Method : ",Dict.keys())
print("Pop() Method : ",Dict.pop(5))
print("Popitem() Method : ",Dict.popitem())
print("Update() Method : ",Dict.update({6:"Finish"}), Dict)
print("Values() Method : ",Dict.values())
