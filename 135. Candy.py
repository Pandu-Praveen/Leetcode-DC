class Solution:
    def candy(self, ratings: List[int]) -> int:
        total = len(ratings)
        pandu = [1] * total

        for i in range(1,total):
            if ratings[i-1] < ratings[i]:
                pandu[i] = pandu[i-1] + 1

        for i in range(total-2,-1,-1):
            if ratings[i+1] < ratings[i] and pandu[i] <= pandu[i+1]:
                pandu[i] = pandu[i+1] + 1
                
        print(pandu)
        return sum(pandu)

        