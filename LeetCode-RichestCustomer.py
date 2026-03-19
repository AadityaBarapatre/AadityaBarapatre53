class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxW=0
        for i in range(len(accounts)):
            w=0
            for j in range(len(accounts[i])):
                w+=accounts[i][j]
            if (w>maxW):
                maxW=w
        return maxW