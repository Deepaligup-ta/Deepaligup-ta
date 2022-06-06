def sum_recur(n):
    if n<=1:
        return n
    else:
        return n+ sum_recur(n-1)

num=int(input("enter the number to find sum"))
print("The sum is",sum_recur(num))
