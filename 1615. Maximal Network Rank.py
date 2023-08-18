class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        arr=[[0]*n for i in range(n)]
        for i in roads:
            src,dst=i
            arr[src][dst]=1
            arr[dst][src]=1

        k=[sum(i) for i in arr]
        ans=[]
        
        for i in range(n):
            for j in range(i+1,n):
                if arr[i][j]==0:
                    ans.append(k[i]+k[j])
                else:
                    ans.append(k[i]+k[j]-1)

        return max(ans)