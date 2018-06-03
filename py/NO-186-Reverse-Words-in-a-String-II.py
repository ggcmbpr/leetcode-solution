class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        """
        fetch each words to a list then reverse and put back to str. not good solution
        """
        str1=[]
        word = []
        for x in str:
            if x != ' ':
                word.append(x)
            else:
                str1.append(word)
                word = []
        str1.append(word)


        indx = 0
        for x in reversed(str1):
            for i in x:
                str[indx] = i
                indx = indx +1

            if indx < len(str):
              str[indx] = ' '
              indx = indx +1


# simple solution from leetcode fastest result
class Solution1(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        str[:] = ' '.join(''.join(str).split(' ')[-1::-1])
