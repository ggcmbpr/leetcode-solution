class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        i = 0
        for x in nums:
            lookfor = target - x
            #if dic.has_key(lookfor):
            if lookfor in dic:
                return [dic.get(lookfor),i]
            else:
                dic.update({nums[i]:i})
            i+=1

#test case
print(Solution().twoSum([1,2,3,4],7))

#resolve it again on 2016/6/3
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cache={}
        for i in range(len(nums)):
            first = target-nums[i]
            if cache.get(first) != None:
                return [cache.get(first),i]
            else:
                cache[nums[i]] = i

#rewrite in clean python style
class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cache={}
        for i,j in enumerate(nums):
            first = target-j
            if first in cache:
                return [cache[first],i]
            else:
                cache[j] = i
