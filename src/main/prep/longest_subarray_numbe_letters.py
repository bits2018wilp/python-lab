
sentence = 'f6sf67isff9p78sfod99syf823'

tmp = [None] * len(sentence)

def maxLen(arr):

    n = len(arr)
    hash_map = {}
    curr_sum = 0
    max_len = 0
    ending_index = -1

    # Traverse through the given array
    for i in range(0, n):

        # Add current element to sum
        curr_sum = curr_sum + arr[i]

        # To handle sum=0 at last index
        if curr_sum == 0 :
            max_len = i + 1  # 0 indexing
            ending_index = i

        if curr_sum not in hash_map:
            hash_map[curr_sum] = i
        else:
            max_len = max(max_len, i - hash_map[curr_sum])
            #ending_index = hash_map[curr_sum]

    print('start index: ', max_len - ending_index, ' len: ', max_len )
    return max_len

for i in range(0, len(sentence)):

    if sentence[i].isdigit():
        tmp[i] = -1
    else:
        tmp[i] = 1

print(tmp)
maxLen(tmp)