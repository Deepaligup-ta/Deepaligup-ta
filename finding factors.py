def factors(x):
    print("The factors of x",x,"are:")
    for i in range(1,x+1):
        if x%i==0:
            print(i)

num=int(input("enter the number to find factors:"))
factors(num)
