# QUICKSORT AND DIVIDE AND CONQUER

# given array of numbers, return total

def total(nums):
    sum = 0

    for num in nums:
        sum += num

    return sum

# how to do this recursively?
# base case: array with 0 or 1 element
# 1. get a list
# if list is empty, return 0
# otherwise, the total sum is the first num in the list + the sum of the rest of the list

# ALSO, pop returns the element popped, not the whole array
# do you have to specify the element you want popped? daheck??

# [1 2 3]
def total2(nums):

    if len(nums) == 0: # 3, 2, 1
        return 0
    else:
        first_num = nums[0]
        nums.pop(0)

        return first_num + total2(nums)
        #         1 .   + 5
        #         2    + 3
        #         3 .  0
        #         []

# data = [1,2,3]
# print("THE DATA, ", total2(data))

# recursive function to count the number of items in a list
# base case: items with 0 or 1
def items_in_list(items):
    sum = 0

    if len(items) == 0:
        return 0
    else:
        return 1 + count(list[1:])

# recursive function to return highest number in list
# base case: 0 or 1 nums
# if empty list, return 0
# otherwise, highest num is searching for

# [1,2,3,4]
def max(list):

    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]   # 3 or 4, return 4
        # return first elem in list or second if greater
    else:
        sub_max = max(list[1:])                             # [2,3,4], [3,4], (is 4), 2 or 4, return 4, 1 or 4, return 4

        return list[0] if list[0] > sub_max else sub_max
        # return first elem in list or the sub_max


# base case : arrays w/ 0 or 1 elem are already sorted
# want to keep calling quicksort until we get one elem in list

# 5, 10, 2 , 4
def quicksort(array):

    if len(array) < 2:
        return array
    else:
        pivot = array[0]                                # 5   ||  # [2]

        # sub-array of all elements less than the pivot
        less = [i for i in array[1:] if i <= pivot]       # [2, 4]  || []
        print("LESS ", less)

        # sub-array of all elements greater than the pivot
        greater = [i for i in array[1:] if i >= pivot]     # [ 10 ]  [4]
        print("GREATER", greater)

        return quicksort(less) + [pivot] + quicksort(greater)       # [2, 4], + [5]  + [10]
                                                                    # [], + [2] + [4]
                                                                    # [2, 4] + 5 + [10]
                                                                    # [2, 4, 5, 10 ]

print(quicksort([5,10,2,4,1,7]))

