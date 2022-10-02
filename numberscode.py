a=int(input("enter a number...."))
b=1
c=0
while b<=a :
    d=b*b                                   #sunny number
    if d==a+1 :
        print("sunny number")
        break
    else:
        print("not sunny number")
        break


a=int(input("enter a number.. "))
b=a*a
c=str(b)[-1]
d=int(c)*int(c)                           #automorphic number
if d==a:
    print("automorphic number")
else:
    print("not a automorphi number")


a=int(input("enter a number.. "))
b=a*a
c=0
e=-1
f=0
while c<=len(str(a)):                              #neon number
    d=str(b)[e]
    f=f+int(d)
    e+=-1
    c=c+1
if f==a:
    print("neon number")
else:
    print("not a neon number")

a=input("enter a number.. ")
b=a[-1::-1]
if a==b:                                           #palindrome number
    print("palindrome number")
else:
    print("not a palindrome number")

a=int(input("enter a number.. "))
b=-1
c1=0
d=0
while d<len(str(a)):
    c=str(a)[b]
    c1=c1+int(c)**3                                #armstrong number
    b+=-1
    d=d+1
if c1==a:
    print("armstrong number")
else:
    print("not a armstrong number")


a=int(input("enter a number.. "))
b=0
c=0
while b<len(str(a)):
    d=str(a)[b]
    c=c+int(d)                                      #harshad number
    b+=1
if a%c==0:
    print("harshad number")
else:
    print("not a harshad number")
    
    
a=int(input("enter a number.. "))
b=0
c=0
e=1
while b<len(str(a)):
    d=str(a)[b]
    c=c+int(d)                                     #spy number
    e=e*int(d)
    b+=1
if c==e:
    print("spy number")
else:
    print("not a spy number")



a=int(input("enter a number"))
b=1
c=0
while b<a:
    if a%b==0:                                     #perfect number
        c=c+b
    b=b+1
if c==a:
    print("perfet number")
else:
    print("not a perect number")