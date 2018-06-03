class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = y = 0
        for step in moves:
            if step == 'L' or step == 'l':
                x = x + 1
            elif step == 'R' or step == 'r':
                x = x - 1
            elif step == 'U' or step == 'u':
                y = y + 1
            elif step == 'D' or step == 'd':
                y = y - 1

        if x == 0 and y == 0:
            return True
        else:
            return False


print( Solution().judgeCircle( 'LLLRRRUUUDDD' ) )
