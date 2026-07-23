
n = int(input("Enter number of elements: "))

print("Enter sorted elements:")
arr = []

for i in range(n):
    arr.append(int(input()))

key = int(input("Enter element to search: "))

# Linear Search
print("\n----- Linear Search -----")
linear = 0

for i in range(n):
    linear += 1
    print("Comparison", linear, ":", arr[i])

    if arr[i] == key:
        print("Element found at position", i + 1)
        break
else:
    print("Element not found")

print("Total Comparisons =", linear)

# Binary Search
print("\n----- Binary Search -----")

low = 0
high = n - 1
binary = 0
found = False

while low <= high:
    mid = (low + high) // 2
    binary += 1

    print("Comparison", binary, ":", arr[mid])

    if arr[mid] == key:
        print("Element found at position", mid + 1)
        found = True
        break
    elif key > arr[mid]:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found")

print("Total Comparisons =", binary)

print("\nTime Complexity")
print("Linear Search : O(n)")
print("Binary Search : O(log n)")
