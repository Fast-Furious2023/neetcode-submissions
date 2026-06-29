import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.count = 0  # timestamp, decremented for max heap
        self.tweets = defaultdict(list)   # userId -> [(count, tweetId)]
        self.following = defaultdict(set) # userId -> {followeeIds}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1  # decrement so most recent = smallest = min heap top

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        
        # include user's own tweets
        self.following[userId].add(userId)
        
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                # start with most recent tweet of each followee
                idx = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][idx]
                # (count, tweetId, followeeId, idx)
                heapq.heappush(heap, (count, tweetId, followeeId, idx))
        
        result = []
        while heap and len(result) < 10:
            count, tweetId, followeeId, idx = heapq.heappop(heap)
            result.append(tweetId)
            
            if idx > 0:  # push next most recent tweet of same user
                idx -= 1
                count, tweetId = self.tweets[followeeId][idx]
                heapq.heappush(heap, (count, tweetId, followeeId, idx))
        
        self.following[userId].discard(userId)  # clean up
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)