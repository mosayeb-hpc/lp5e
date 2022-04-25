# insersion sort implementation in python 3

arr = [6,9,4,1,0,3,8,2,5,7]
key = 0
i = 0
j = 0

def ins_sort(arr):
    arr1 = arr[:]
    for i in range(1, len(arr1)):
        key = arr1[i]
        for j in range(i - 1, -1, -1):
            if key < arr1[j]:
                arr1[j+1]=arr1[j]
            else:
                break

        if(j + 1 == i):
            pass
        else:
            arr1[j] = key
    return arr1

#ins_sort(arr)
#for i in range(len(arr)):
#    print(arr[i], sep=', ', end='')
