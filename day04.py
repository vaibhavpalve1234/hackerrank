# # array

# # # declaration
# # fruits = ["apple", "banana", "pineapple"]

# # # or 
# fruits = list()
# print(fruits)
# fruits.append("apple")
# print(fruits)
# fruits.append("banana")
# print(fruits)
# fruits.append("pineapple")
# print(fruits)

# # # # or
# # fruits = list()
# # apple = ["red apple", "green apple"] 
# # banana = ["red banana", "yellow_banana"]
# # pineable = ["pineapple"]

# # fruits.extend(apple)
# # fruits.extend(banana)
# # fruits.extend(pineable)

# # print(fruits)

############ 

# + -> 5 + 7 = 12
# + -> "ram" + "rohan" = ratrohan
# + -> to data types are of list then it will behave like extend

# summer_fruits = ["apple", "banana"]
# winter_fruits = ["grapes", "mango"]

# fruits = summer_fruits + winter_fruits

# print("summer fruits ", summer_fruits)

# print("winter fruits ", winter_fruits)

# print("all fruits ", fruits)


# a = [1,2,3,4]
# b = ["a", "b", "c", "d"]
# c = a + b
# a = "a"
# b = "b"
# c = "c"
# d = "d"
# b = [a, b, c, d]


a = ["abc", "def"]
b = [3, 4, str(5) + "s"]
c = a.extend(b)
print(c)
print(a)
print(b)
c= a+b
print(c)
