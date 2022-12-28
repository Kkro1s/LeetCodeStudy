def removeElement(nums, val):
    a = 0
    while a < len(nums):
        if a == len(nums):
            break
        elif nums[a] == val:
            del nums[a]
        else:
            a += 1
    print(len(nums), nums)

removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)


"""

28/12/2022

learn three main loops



"""