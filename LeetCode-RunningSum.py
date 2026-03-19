class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp=0
        Output=[]
        for i in range(len(nums)):
            temp=temp+nums[i]
            Output.append(temp)
        return Output