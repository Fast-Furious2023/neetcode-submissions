from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) #userid:[(count,tweetid)]
        self.following = defaultdict(set) #userid:{followees}
        self.count = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweets[userId].append((self.count, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = [] # size 10

        followees = self.following[userId]
        for followee in followees | {userId}:
            if followee in self.tweets:
                indx = len(self.tweets[followee])-1
                count, tweetid = self.tweets[followee][indx]
                heapq.heappush(heap, [count, tweetid, followee, indx])
        
        res = []
        while heap and len(res) < 10:
            count, tweetid, followee, indx = heapq.heappop(heap)
            res.append(tweetid)
            if indx > 0:
                count, tweetid = self.tweets[followee][indx-1]
                heapq.heappush(heap, [count, tweetid, followee, indx-1])
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
