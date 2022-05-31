n=int(input("enter the limit of natural numbers to find:"))
result=list(map(lambda x:2**x, range(n)))
print("the total terms are:",n)
for i in range(n):
    print("2 raised to power",i,"is",result[i])

