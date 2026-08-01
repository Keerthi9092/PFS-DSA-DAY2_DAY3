#delete operation in array with constrains -> (1<=i<= 20)
# capacity = 20
# arr = [0] * capacity
# n = int(input("Enter the size of the array(max 20) : "))
# for i in range(n):
#     arr[i] = int(input(f"Enter element {i}:"))
# size = n
# pos = int(input("Enter the index value:"))
# if size ==0:
#     print("Array is Empty")
# elif pos<0 or pos>=size:
#     print("Invalid index....")
# else:
#     delete =arr[pos]
#     for i in range(pos, size-1): #size-1(to delete the last element) and pos(to delete the element at given index)))
#         arr[i] = arr[i+1]
#     size -= 1
#     print("Deleted element is:", delete)
# for i in range(size):
#     print(arr[i], end = " ")

#write a program to perform linear search in an array and print the index value found
# arr = list(map(int, input("Enter elements: ").split()))
# target = int(input("Enter target element"))
# for i in range(len(arr)):
#     if arr[i] == target:
#         print(target,"found at index:", i)
#         break

        
#Given an array nums of integers, return how many of them contain an even number of digits.
'''nums = list(map(int, input("Enter numbers: ").split())) 
count = 0
for i in nums:
    if len(str(i)) % 2 == 0:
        count += 1
print(count)'''

# ==========================================
# Day 2 - Array Data Structure Operations
# Date: 16-06-2026
# ==========================================

# -------------------------------
# 1. Insert at Beginning
# -------------------------------
arr = list(map(int, input("Enter array: ").split()))
x = int(input("Enter element to insert at beginning: "))

arr.append(0)
for i in range(len(arr)-1, 0, -1):
    arr[i] = arr[i-1]
arr[0] = x

print("After inserting at beginning:", arr)


# -------------------------------
# 2. Insert at End
# -------------------------------
arr = list(map(int, input("\nEnter array: ").split()))
x = int(input("Enter element to insert at end: "))

arr.append(x)

print("After inserting at end:", arr)


# -------------------------------
# 3. Delete from Beginning
# -------------------------------
arr = list(map(int, input("\nEnter array: ").split()))

for i in range(len(arr)-1):
    arr[i] = arr[i+1]

arr.pop()

print("After deleting from beginning:", arr)


# -------------------------------
# 4. Delete from End
# -------------------------------
arr = list(map(int, input("\nEnter array: ").split()))

arr.pop()

print("After deleting from end:", arr)


# -------------------------------
# 5. Insert by Position
# -------------------------------
arr = list(map(int, input("\nEnter array: ").split()))
pos = int(input("Enter position: "))
value = int(input("Enter value: "))

arr.append(0)

for i in range(len(arr)-1, pos, -1):
    arr[i] = arr[i-1]

arr[pos] = value

print("After insertion:", arr)


# -------------------------------
# 6. Delete by Position
# -------------------------------
arr = list(map(int, input("\nEnter array: ").split()))
pos = int(input("Enter position to delete: "))

for i in range(pos, len(arr)-1):
    arr[i] = arr[i+1]

arr.pop()

print("After deletion:", arr)


# -------------------------------
# 7. Delete by Value
# -------------------------------
arr = list(map(int, input("\nEnter array: ").split()))
value = int(input("Enter value to delete: "))

if value in arr:
    index = arr.index(value)

    for i in range(index, len(arr)-1):
        arr[i] = arr[i+1]

    arr.pop()
    print("After deletion:", arr)
else:
    print("Value not found")


# -------------------------------
# 8. Search
# -------------------------------
arr = list(map(int, input("\nEnter array: ").split()))
key = int(input("Enter element to search: "))

flag = False

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at index", i)
        flag = True
        break

if not flag:
    print("Element not found")


# -------------------------------
# 9. Update
# -------------------------------
arr = list(map(int, input("\nEnter array: ").split()))
pos = int(input("Enter position: "))
value = int(input("Enter new value: "))

arr[pos] = value

print("Updated array:", arr)


# -------------------------------
# 10. Reverse Array
# -------------------------------
arr = list(map(int, input("\nEnter array: ").split()))

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print("Reversed array:", arr)


# -------------------------------
# 11. Rotate Left (1 Position)
# -------------------------------
arr = list(map(int, input("\nEnter array: ").split()))

first = arr[0]

for i in range(len(arr)-1):
    arr[i] = arr[i+1]

arr[-1] = first

print("Left Rotation:", arr)


# -------------------------------
# 12. Rotate Right (1 Position)
# -------------------------------
arr = list(map(int, input("\nEnter array: ").split()))

last = arr[-1]

arr.append(0)

for i in range(len(arr)-2, -1, -1):
    arr[i+1] = arr[i]

arr[0] = last

arr.pop()

print("Right Rotation:", arr)
        