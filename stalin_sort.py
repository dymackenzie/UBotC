arr = [3, 5, 20, 15, 9, 120, 30]

a = 0
for i in range(len(arr)):
    i = i - a
    if arr[i] < arr[i-1]:
        arr.pop()
        a+=1


# base = arr[0]
# toRemove = list()
# for i in range(1, len(arr)):
#     if arr[i] < base:
#         toRemove.append(i)
#     else:
#         base = arr[i]

# for i in toRemove:
#     arr.pop(i)

# print(arr)
    
