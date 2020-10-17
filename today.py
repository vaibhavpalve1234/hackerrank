# def sol1(n,str):
#     if len(str)==2*n:
#         return str
#     sol1(n,str+"(")
#     sol1(n,str+")")

# def sol(op,cp,n):
#   if op+cp==2*n:
#     a=(sol1(op+cp,""))
#     print(a)
#     return 1
#   p1=sol(op+1,cp,n)
#   p2=sol(op,cp+1,n)
#   return p1+p2

# sol(0,1,2)
def sol(str,res,isstart):
    if len(str)==0:
        print(str,end="$")
        return
        
    sol(str[1:]+res+str[0],"",False)
    if not isstart:
        sol(str[1:]+res+""+str[0],"",False)

sol("abc"," ",True)

    