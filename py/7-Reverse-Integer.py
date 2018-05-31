class Solution:
    def reverse_depricated(self, x):
        """
        :type x: int
        :rtype: int
        """
        # verify positive or minus
        flag = False
        if x < 0:
            flag = True
            x = abs(x)
        #revert
        temp = x % 10
        rc = 0
        while x / 10 > 0:
            rc = rc*10 + 10 * temp
            x = x / 10
            temp = x % 10

        rc = rc + temp

        #final check to make sure within range
        if flag is True:
            rc = -rc

        if rc > 2 ** 31 -1 or rc < - 2 ** 31:
            rc = 0

        return rc

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # verify positive or minus
        flag = False
        if x < 0:
            flag = True
            x = abs(x)
        #revert
        rc = 0
        while x > 0:
            temp = x%10
            rc=rc*10+temp
            x=x/10

        #final check to make sure within range
        if flag is True:
            rc = -rc

        if rc > 2 ** 31 -1 or rc < - 2 ** 31:
            rc = 0

        return rc

print(Solution().reverse(1234))
