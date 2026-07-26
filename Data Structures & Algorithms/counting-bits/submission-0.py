class Solution:
    def countBits(self, n: int) -> List[int]:
        output=[0]*(n+1)
        next = 4
        power = 1
        for i in range(n+1):
            if i == 0: 
                output[i]=0
            elif i == 1: 
                output[i]=1
            elif i == 2: 
                output[i]=1
            elif i < next: 
                output[i]=1+output[i-pow(2, power)]
            else:
                output[i]=1
                next = next*2
                power+=1
        return output

            
            