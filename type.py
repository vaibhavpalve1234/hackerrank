#Write the calculator program which will take input from users two numbers
#And will ask them to type
#0 for addition
#1 for subtraction
#2 for multiplication
#3 for division
#And will print the result

a=int(input('enter a nu.'))
b=int(input('enter 2nd nu.'))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)



#Explain range in python with various examples ..
#range(start,end )
#range (start,end,step)
#range(start: int, stop: int, step: int=...)
#range(stop) -> range object
#range(start, stop[, step]) -> range object
#Return an object that produces a sequence of integers from start (inclusive)
#to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
#start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
#These are exactly the valid indices for a list of 4 elements.
#When step is given, it specifies the increment (or decrement).
#eg.
#range(1,5,1)
#ans :-1 2 3 4



#What will be the result of
#int(6.6) + int(4.9) = ?
#ans is 10