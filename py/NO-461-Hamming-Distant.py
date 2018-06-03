class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        rc = 0
        z = x^y
        while(z>0):
            if (z&1):
                rc+=1

            z>>=1

        return rc
