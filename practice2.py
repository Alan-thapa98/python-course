apples=int(input("Enter the number of apples:\n "))
mn=int(input("enter the minimum number of apples to cheak:\n"))
mx=int(input("enter the maximum number of apples to cheak:\n"))
for i in range(mn,mx+1):
    if apples%i==0:
        print(f"{i} is divisor of {apples}")
    else:
        print(f"{i} is not divisor of {apples}")

