class Solution(object):
    def twoSum(self, nums, target):
        """
        24/12/2022
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lens = len(nums)
        for i in range(lens):
            for j in range(i + 1, lens):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


""" 
i in range(10):
方法一暴力拆解，遍历两次直到找到对应的值，学习 rang方法

range(start, stop, step)
range()是一个内置函数，可以生成一个整数序列。它有三个参数：起始值，结束值，步长。
 to generate a sequence of numbers from 0 to 9 (not including 9), you can use the following code:

for
    print(i)

则它会返回所有的从0 - 9，一共十个数

To generate a sequence of numbers from 2 to 9 (not including 9), you can use the following code:

for i in range(2, 10):
    print(i)

返回从2开始到9（不包括9）

To generate a sequence of numbers from 2 to 9 (not including 9) with a step of 2, you can use the following code:

Copy code
for i in range(2, 10, 2):
    print(i)

生成2-9 的数步长为2
2
4
6
8
"""