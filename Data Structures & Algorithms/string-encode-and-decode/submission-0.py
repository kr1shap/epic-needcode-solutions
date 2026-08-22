class Solution:

    def encode(self, strs: List[str]) -> str:
        final_msg = ""
        for msg in strs: 
            length = len(msg)
            final_msg += str(length) + "#" + msg
        return final_msg

    def decode(self, s: str) -> List[str]:
        num = ""
        i = 0
        res = []
        msg = ""
        while i < len(s): 
            char = s[i]
            if char in "1234567890":
                num+=char
                i+=1
            elif char == "#":
                j = 0
                i+=1
                while j < int(num):
                    msg += s[i+j]
                    j+=1
                res.append(msg)
                i+= int(num)
                msg = ""
                num = ""
            else: 
                i+=1
                
        return res

