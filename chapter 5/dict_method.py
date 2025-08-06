# 1

dict_method = { "abhi" : 100, "jit": 98, "rahul": 55, "aditay": "yash" }

print(dict_method.get("abhi"))  # Using get method to access value

# 2

print(dict_method.keys())  # Using keys method to get all keys

# 3 

print(dict_method.values())  # Using values method to get all values


# 4 

print(dict_method.items())  # Using items method to get all key-value pairs


#5

print(dict_method.pop("jit"))  # Using pop method to remove a key-value pair and return the value


#6

print(dict_method.popitem())  # Using popitem method to remove and return the last inserted key-value pair


# 7

# dict_method = { "abhi" : 100, "jit": 98, "rahul": 55, "aditay": "yash" }

# dict_method.update({"abhi" : 133})

# print(dict_method)