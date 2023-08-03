class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # Creating a hash map with phone key and their respective values.
        dict={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}

        # Take the values for each phone key of the given stirng.
        total=[dict.get(int(i)) for i in digits]

        # If the input is empty, then empty array should be our answer.
        if total==[]: return []

        answer=[]
        def check(arr,k):
            if k==len(total):
                answer.append(arr[:])
                return

            for i in range(len(total[k])):
                # Recursively call the function until reaching the length of [total] array.
                check(arr+total[k][i],k+1)

        check('',0)
        return answer