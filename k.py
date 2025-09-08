import random
s=random.randint(1,30)
c=0
a=True
while True:
    b=int(input())
    c+=1
    if b<s:
        print("low")
    elif b>s:
        print("High")
    elif b==s:
        a=False
        print("found")
        print(c)
        break