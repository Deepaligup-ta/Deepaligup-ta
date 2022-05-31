n=int(input("enter the series number:"))
n1,n2=0,1
count=0

if(n<=0):
    print("enter the positive number")
elif(n==1):
    print(n1)
else:
    print("fibinocai series")
    while count<n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1
        
