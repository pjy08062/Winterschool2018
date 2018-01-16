import turtle as t


b=int(input("몇각형입니까?"))
a=360/b
i=0
while i<b:
    t.fd(20)
    t.lt(a)
    i+=1
