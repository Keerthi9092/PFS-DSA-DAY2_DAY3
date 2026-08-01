#insert at beginning
'''n=3
arr = 10 20 30
x = 5
output = 5 10 20 30'''

'''arr = [10, 20, 30]
x = 5
arr.insert(0, x)
print(arr)'''

'''arr = list(map(int, input("Enter numbers: ").split()))
n = int(input("Enter a number to append at left: "))
arr.append(0)  # Increase the size of the array by 1
for i in range(len(arr) - 1, 0, -1):
    arr[i] = arr[i - 1]  # Shift elements to the right
arr[0] = n  # Insert the new element at the beginning
print(arr)'''
