class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=0
        n=len(str(x))
        X=x
        for i in range(n):
            a=x%10
            b=a*10**(n-i-1)
            temp=temp+b
            x=x//10
        return X==temp