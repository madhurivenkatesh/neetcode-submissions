class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if(len(nums)<=1):
            return False
        nums_s=sorted(nums)
        prev=0
        i=1
        while(i<len(nums_s)):
            if(nums_s[i]==nums_s[prev]):
                return True
            prev=i
            i+=1
        return False
