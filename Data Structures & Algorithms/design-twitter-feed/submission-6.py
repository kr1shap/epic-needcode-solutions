from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        # map user to the ppl who follow them 
        self.followees = defaultdict(set) 
        # map user to the people who they follow
        self.followers = defaultdict(set)
        # map user to their tweets
        self.tweets = defaultdict(list)
        # counter 
        self.count = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.count, -tweetId))
        self.count+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        pq = []
        # get list of followers in userId
        followers = self.followers[userId]
        counter = defaultdict(int) # follower to index 
        done = 0
        # append the first one of each 
        for fol in followers: 
            if self.tweets[fol]: 
                cnt, tweet = self.tweets[fol][-1]
                pq.append((cnt, tweet, fol))
            counter[fol] = len(self.tweets[fol]) - 1

        if self.tweets[userId]:
            cnt, tweet = self.tweets[userId][-1]
            pq.append((cnt, tweet, userId))
            counter[userId] = len(self.tweets[userId]) - 1

        heapq.heapify(pq)

        while len(res) != 10 and done != len(followers) + 1 and pq:
            # pop first one 
            _, tweet, follower = heapq.heappop(pq)
            res.append(-tweet)
            counter[follower]-=1
            if counter[follower] < 0: 
                done+=1
                continue
            else: 
                idx = counter[follower]
                cnt, tweet = self.tweets[follower][idx]
                heapq.heappush(pq, (cnt, tweet, follower))

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        self.followees[followeeId].add(followerId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
            self.followees[followeeId].remove(followerId)

        
