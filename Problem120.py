class Solution(object):
    def minimumTotal(self, triangle):
        dp = triangle[-1][:]

        
        row = len(triangle)-2

        while row>=0:
            col=0
            while col <len(triangle[row]):

                dp[col] = triangle[row][col] + min(dp[col],dp[col+1])
                col+=1
            row-=1

        return dp[0]
