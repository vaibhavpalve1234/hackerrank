
# count string lenght
# def sol(str):
#     if str=="":
#         return 0
#     return 1+sol(str[1:])
# print(sol(input(" enter a name :")))

# def sol(op,cp,n):
#     if op < cp:
#         return 0
#     if op+ cp == 2*n :
#         if op == cp :
#             return 1
#         return 0

#     a=sol(op+1,cp,n)
#     b=sol(op,cp+1,n)
#     return a+b
# print(sol(0,0,13))

# def sol(str,n):
#     if len(str) == 2*n:
#         print(str)
#         return 
#     sol(str+"0",n)
#     sol(str+"1",n)

# sol("",5)

min_step=10000001
def sol(a,b,c,step):
    global min_step
    if a-1==b or a-2==b:
	    min_step=min(step,min_step)
        
	    return 
    if a>b:
    	sol(a-1,b,c,step)
	    
        sol(a-2,b,c,step)

    else :
        sol(a*c,b,c,step)
        sol(a-2,b,c,step)
        sol(s-1,b,c,step)

t=int(input())
while t >0:
    a,b,c=map(int,input().split())
    sol(a,b,c,0)
    t-=1
