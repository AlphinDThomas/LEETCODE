class Solution(object):
    def minimumTotal(self, triangle):
        #store last row into dp
        dp = triangle[-1][:]

        #start from second last row
        row = len(triangle)-2

        while row>=0:         #checks from below , so if there are rows above check again
            col=0
            while col <len(triangle[row]):

                dp[col] = triangle[row][col] + min(dp[col],dp[col+1]) #replaces each element in dp starting from 
                col+=1                                                #first element to the length of the row above
            row-=1

        return dp[0]

# Example:
#
# triangle = [
#     [2],
#     [3,4],
#     [6,5,7],
#     [4,1,8,3]
# ]
#
# Step 1:
# dp = last row = [4,1,8,3]
#
# Step 2: row = 2 -> [6,5,7]
#
# dp[0] = 6 + min(4,1) = 7
# dp[1] = 5 + min(1,8) = 6
# dp[2] = 7 + min(8,3) = 10
#
# dp becomes:
# [7,6,10,3]
#
# Step 3: row = 1 -> [3,4]
#
# dp[0] = 3 + min(7,6) = 9
# dp[1] = 4 + min(6,10) = 10
#
# dp becomes:
# [9,10,10,3]
#
# Step 4: row = 0 -> [2]
#
# dp[0] = 2 + min(9,10) = 11
#
# dp becomes:
# [11,10,10,3]
#
# Answer:
# dp[0] = 11
#
# Idea:
# dp[col] stores the minimum path sum from that position
# in the current row down to the bottom.
# We start from the last row and move upward,
# updating dp in-place.