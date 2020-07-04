import array
arr = array.array('i', [1,2,3])

print("The new array created is: ")
for i in range(0,3):
    print(arr[i])

print("\r")

arr.append(4)

print("The appended array is: ")
for i in range(0,4):
    print(arr[i])


arr.insert(2,5)


print("The  inserted array is: ")
for i in range(0,5):
    print(arr[i])
