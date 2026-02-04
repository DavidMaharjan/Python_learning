x= int(input("Enter X-axis dimension:"))
y= int(input("Enter Y-axis dimension:"))
z= int(input("Enter Z-axis dimension:"))
combinations= []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            combinations.append((i,j,k))

print(combinations)
n= int(input("Enter the axis length:"))
filtered_combinations=filter(lambda a: sum(a)!=n, combinations)
print(sorted(list(filtered_combinations)))