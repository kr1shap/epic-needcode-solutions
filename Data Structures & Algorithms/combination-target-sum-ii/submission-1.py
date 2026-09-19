class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)

        def backtrack(index: int, arr: List[int], sum: int) -> None: 
            if index >= len(candidates):
                if sum == target:
                    res.append(arr.copy())
                return
            arr2 = arr + [candidates[index]]
            # print(arr2)
            if candidates[index] + sum == target: 
                res.append(arr2)
                return
            if candidates[index] + sum > target: 
                return

            for i in range(index+1, n):
                if candidates[index] == candidates[i]:
                    continue
                else: 
                    backtrack(i, arr[:], sum)
                    break
            backtrack(index+1, arr2, sum + candidates[index])
        

        backtrack(0, [], 0)

        return res