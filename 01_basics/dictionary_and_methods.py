# dict1 = {} #empty dictionary
# a = set() #empty set
# print(dict1,type(dict1))
# print(a,type(a))

dict1 = {"good":"something pleasant", "fetch":"to bring"} #dict = {"key1":value1,"key2":value2}
dict2 = {"Tamal": 99,"Anirban":89,"nil":98}
print(dict1,dict2)

#tip : dictionaries are mutable i.e. it can be modified.

dict2["Priyanka"] = 34
print(dict2)

print(dict2.get("Priyanka"))
print(dict2.keys())
print(dict2.values())
print(dict2.items())