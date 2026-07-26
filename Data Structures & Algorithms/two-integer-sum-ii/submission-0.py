class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointer problem 
        i = 0
        j = len(numbers)-1
        while i < j: 
            s = numbers[i] + numbers[j]
            if s < target: 
                i+=1
            elif s > target: 
                j-=1
            elif s == target:
                return [i+1, j+1]
        return []