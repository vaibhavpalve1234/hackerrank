# def honai(n,s,i,e):
#     if n==0:
#         return 1
#     honai(n-1,s,i,e)
#     move(s,i)
#     honai(n-1,s,i)
# honai(4,"a","b","c")


# while True:
#     n=int(input())
#     if n==42 :
#         break
#     else :
#         print(n)


n=int(input())
for i in range(n):
    c=input()
    print(int(c[::-1]))