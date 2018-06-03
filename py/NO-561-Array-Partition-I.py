class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        rc = i = 0
        for x in nums:
            if i%2 is 0:
                rc += x
            i+=1
        return rc
