class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_arr = sorted(nums)
        nums_d ={}
        
        i=0
        while(i<len(nums_arr)):
            val=nums_arr[i]
            nums_d.setdefault(val,0)
            nums_d[val]+=1
            i+=1

        sorted_l= nums_d.items()
        sorted_l=sorted(sorted_l,key=lambda item: item[1],reverse=True)
        ans=[]
        for i in range(0,k):
            ans.append(sorted_l[i][0])

        return ans
            

        