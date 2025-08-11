class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        arr=[]
        res=[]
        mod=10**9+7
        while n!=0:
            p=pow(2,floor(log2(n)))
            arr.append(p)
            n=n-p
        arr.append(1)
        arr=arr[::-1]
        for i in range(1,len(arr)):
            arr[i]=arr[i]*arr[i-1]
        for left,right in queries:
            init=arr[right+1]//arr[left]
            res.append(init%mod)
        return res


