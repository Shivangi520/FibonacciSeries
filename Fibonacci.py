def Fibonacci(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return (Fibonacci(n-2) + Fibonacci(n-1))

n=(input("Enter the number of terms you want in you series:"))
if(n.isdigit() and (int(n)>0)):
    n=int(n)
    for i in range(1,n+1):
        print(Fibonacci(i),end=' ')
else:
    print("Not a valid series")
