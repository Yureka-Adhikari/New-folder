def findmin(a,size):
    temp = a[0]
    for i in range(1, size):
        temp = min(temp, a[i])
    return temp

def findmax(a,size):
    temp = a[0]
    for i in range(1, size):
        temp = max(temp, a[i])
    return temp

a = [12,3,45,67,90,99,1090]
size = len(a)

print("Minimum of the array is:", findmin(a, size))
print("Maximum of the array is:", findmax(a, size))