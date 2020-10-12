def check(str):
    cp=0
    op=0
    for i in range(len(str)):
        if str[i]=="(":
            cp+=1
        else:
            op+=1
        if op>cp:
            return False
    return op==cp
def sol(n,str):
    if len(str)==2*n:
        if check(str):
            print(str)
        return
    sol(n,str+"(")
    sol(n,str+")")
    
sol(10,"")