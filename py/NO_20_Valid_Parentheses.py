class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = list(s)
        stack = []
        for i in l:
            left = ''
            if i in ['(','{','[']:
                stack.append(i)
                continue
            elif len(stack)>0:
                left = stack.pop()
            else:
                return False

            if [left,i] not in [['(', ')'], ['{', '}'], ['[',']']]:
                return False
        if len(stack)>0:
            return False
        return True

