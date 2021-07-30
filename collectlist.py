a = [1, 212, 324, 35, 4, 6, 67, 80, 1, 3, 4, 5, 78, 89]

# b=[]

# for item in a:
#     if item%2==0:
#         b.append(item)
b = [i for i in a if i % 2 == 0]
print(b)
