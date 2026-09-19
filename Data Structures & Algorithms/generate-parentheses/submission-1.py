class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        #)(
        # ()()())(

        def backtrack(s: str, front: int, back: int):
            if back > front: 
                return 
            if back + front > 2*n: 
                return
            if back == n and front == n: 
                res.append(s[:])
                return
            backtrack(s + "(", front + 1, back)
            backtrack(s + ")", front, back + 1)
           
        backtrack("", 0, 0)
        return res
