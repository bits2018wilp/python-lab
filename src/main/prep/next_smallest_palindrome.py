
def apply_even(arr):

    arr1 = arr[:len(arr)//2]
    arr2 = arr[len(arr)//2:]
    print(arr1)
    print(arr2)

def apply_odd(arr):

    print(arr)

    arr1 = arr[:len(arr)//2]
    arr2 = arr[(len(arr)//2)+1:]

    print(arr1)
    print(arr2)

    tmp = arr1.copy()
    tmp.reverse()
    print(arr1, tmp)

    if int("".join(str(x) for x in arr2)) <  int("".join(str(x) for x in tmp)):

        print(arr1,arr[len(arr)//2], tmp)

    else:

        if arr[len(arr)//2] < 9:
            print(arr1, arr[len(arr)//2]+1, tmp)
        else:
            j = len(arr1)-1
            i = 0

            while j >=0:

                if arr1[j] < 8:
                    arr1[j] = arr1[j]+1
                    tmp[i] = tmp[i]+1
                    break
                else:
                    arr1[j] = 0
                    tmp[i] = 0
                    j-=1
                    i+=1
            if sum(arr1+[0]+tmp) == 0:
                print([1]+arr1+[0]+tmp+[1])
            else:
                print(arr1, 0, tmp)

arr = [9, 4, 1, 8, 7, 9, 7, 8, 3, 2, 2]
# arr = [3,2,2,7,1,4,9]
# arr = [2,1,3,5,4]
# arr = [9,9,1,8,9]
# arr = [5,4,3,2,1]
arr = [9,9,9,9,9]

# 99189
# 21354  21412
# 78565  78587
# 941 9 322    941 9 149  942 0 149  942 0 249
# 941 7 322    941 8 149
# 322 7 941    322 7 223  322 8 223
# 322 9 941    322 9 223  323 0 223   323 0 323
# 94187 9 78322  => 94187 9 78149  => 94188 0 78149  => 94188 0 88149
# 94187 9 98322  => 94189 9 98149  => 94190 0 98149  => 94190 0 90149

if len(arr) %2 ==0:
    apply_even(arr)
else:
    apply_odd(arr)
