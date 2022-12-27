def deleteDuplicates(nums):
    lens = len(nums)
    ind = 0
    next = 1
    while next < lens:
        while nums[ind] == nums[next]:
            del nums[next]
        ind += 1
        next +=1
        lens = len(nums)



    print(len(nums), nums)

deleteDuplicates([0,0,1,1,1,2,2,3,3,4,5,5,5,5,5,6,6,7,8,9])
"""

27/12/2022
learn how to delete element from a list

use del[index]

if I want remove some element

use del[index1: index2]
them it moves each element from index2 - index1


also remove specific element like.remove(element)


"""