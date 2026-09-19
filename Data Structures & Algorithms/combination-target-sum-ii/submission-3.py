class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)

        def backtrack(index: int, arr: List[int], sum: int) -> None:
            if sum == target:
                res.append(arr.copy())
                return 
            if index >= len(candidates):
                return
            arr2 = arr + [candidates[index]]
            if candidates[index] + sum == target: 
                res.append(arr2)
                return
            if candidates[index] + sum > target: 
                return

            # for loop is excluding this specfic number and all instances of it 
            for i in range(index+1, n):
                if candidates[index] == candidates[i]:
                    continue
                else: 
                    backtrack(i, arr[:], sum)
                    break
            # this loop allows for dupes, including the number
            # if there is only one instance of this number 
            # still acts differently than above loop 
            backtrack(index+1, arr2, sum + candidates[index])
        

        backtrack(0, [], 0)

        return res