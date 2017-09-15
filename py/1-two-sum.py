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
