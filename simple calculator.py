import math
print("\t____calcluator_____")
def sum(a,b):
    a=a+b
    return a
def sub(a,b):
    if(a>b):
        a=a-b
        return a
    else:
        b=b-a
        return b
def mul(a,b):
    a=a*b
    return a
def div(a,b):
    q=a/b
    r=a%b
    print("\nThe quotient is :%s"%q)
    print("\nThe remainder is:%s"%r)

def sqr(a):
    x=math.sqrt(a)
    return x
def pow(a,b):
    a=math.pow(a,b)
    return a

while(True):
    print("\n\nchoose the operation you want to perform:")
    print("\n\t1.Addition")
    print("\n\t2.substraction")
    print("\n\t3.multiplication")
    print("\n\t4.division")
    print("\n\t5.square")
    print("\n\t6.square root")
    print("\n\t1.exit")
    choice=int(input(">"))
    if choice==1:
        print("\n\nenter two numbers:")
        num1=int(input(">"))
        num2=int(input(">"))
        s=sum(num1,num2)
        print("the sum is:%s"%s)
    elif choice==2:
        print("\n\nenter two numbers:")
        num1=int(input(">"))
        num2=int(input(">"))
        m=sub(num1,num2)
        print("the substraction is:%s"%m)
    elif choice==3:
        print("\n\nenter two numbers:")
        num1=int(input(">"))
        num2=int(input(">"))
        p=mul(num1,num2)
        print("the multiplication is:%s"%p)
    elif choice==4:
        print("\n\nenter two numbers:")
        num1=int(input(">"))
        num2=int(input(">"))
        div(num1,num2)
    elif choice==6:
        print("\n\nenter two numbers:")
        num1=int(input(">"))
        r=sqr(num1)
        print("the sqrt is:%s"%r)
    elif choice==5:
        print("\n\nenter a numbers:")
        num1=int(input(">"))
        num2=int(input(">"))
        t=pow(num1,num2)
        print("the exponent is:%s"%t)
    else:
        print("\n you choose to exit.byee")
        break
    
    
    
    
        
        

