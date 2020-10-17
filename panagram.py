n=input()

a=set(str.lower(n))
if len(a)==27 :
    print("pangram")

else:    print("not pangram")