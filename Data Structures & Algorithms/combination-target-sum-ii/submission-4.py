class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        # target = 4 [2, 2, 2]

        # [] go into [2] or [none]
        # [2] go into [2] or [2, 2]
        # [2, 2] -> [2, 2, 2] or [2, 2]
        def dfs(index: int, curr: list[int], sum: int):
            if sum == target:
                res.append(curr[:])
                return
            if index >= len(candidates):
                return
            if candidates[index] + sum > target:
                return 
            # case 1: add current candidate 
            amt = candidates[index]
            arr = curr[:]
            arr.append(amt)
            dfs(index+1, arr, sum + amt)
            # case 2: skip all instances of current candidate 
            prev = candidates[index]
            index+=1
            while index < len(candidates) and prev == candidates[index]:
                prev = candidates[index]
                index+=1
            if index < len(candidates):
                print(curr, candidates[index])
            dfs(index, curr[:], sum)
        
        for i in range(len(candidates)):
            if i > 0 and candidates[i-1] == candidates[i]:
                continue
            else:
                dfs(i+1, [candidates[i]], candidates[i])
        return res
        