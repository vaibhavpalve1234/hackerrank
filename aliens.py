# x=4
# for i in range(x):
#     if i%2==0:
#         for j in range(i+1):
#                 print("#",end="")
#     else :
#         for j in range(i+1):
#             print(j,end="")
#     print("")
# for i in range(x):
#     if i%2==0:
#         for j in range(i-1):
#                 print("#",end="")
#     else :
#         for j in range(i-1):
#             print(j,end="")
#     print("")



# # for i in range(x):
# #     for j in range(x-i):
# #         if j%2==0:
# #             print(j,end="")
# #         else :
# #             print(" #",end="")
# #     print("")



x=int(input(" enter a no :"))
for i in range(2,x):
    if x%i==0:
        print("not prime")
else :
    print("prime")