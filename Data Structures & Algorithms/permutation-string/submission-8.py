class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #get freq table 
        if len(s1) > len(s2):
            return False
        if s1 == s2: 
            return True
        freq = {}
        for char in s1:
            freq[char] = freq.get(char, 0) + 1
        print(freq)
        i = 0
        j = 0
        # while i < len(s2) and j < len(s2):
        #     print(s2[i:j])
        #     if(len(s2[i:j]) < len())
        #     #create hashmap of s2 substring
        #     temp = {}
        #     for char in s2[i:j+1]:
        #         temp[char] = temp.get(char, 0) + 1
        #         print(temp)
        #         if temp == freq:
        #             return True
        #         elif 
        #         i+=1
        for i in range(0, len(s2)):
            if s2[i] in freq: 
                #create hashmap of s2 substring
                temp = {}
                for char in s2[i:i+len(s1)]:
                    temp[char] = temp.get(char, 0) + 1
                print(temp)
                if temp == freq: 
                    return True
        return False
                
            

        
