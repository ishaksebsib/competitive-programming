class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans=[]
        for i in range(len(l)):
            p=l[i]
            q=r[i]
            arr=nums[p:q+1]
            arr=sorted(arr)
            m=arr[1]-arr[0]
            f=1
            for i in range(2,len(arr)):
                if((arr[i]-arr[i-1])!=m):
                    f=0
                    ans.append(False)
                    break
            if(f):
                ans.append(True)
        return ans
