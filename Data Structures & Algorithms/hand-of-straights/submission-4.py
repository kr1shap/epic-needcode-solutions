from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: 
            return False # uneven groupings
        hand.sort()
        # map ele in hand to hashmap freq
        freq = defaultdict(int)
        maxVal = hand[-1]
        minVal = hand[0]
        for ele in hand: 
            freq[ele]+=1
        
        # do groupings? 
        numGroups = 0
        for val in hand:
            isValidGp = False
            for i in range(groupSize):
                if freq[val+i] <= 0: 
                    isValidGp = False
                    break
                isValidGp = True
            if isValidGp: 
                numGroups+=1
                for i in range(groupSize):
                    freq[val+i]-=1
        return (len(hand) / groupSize) == numGroups

