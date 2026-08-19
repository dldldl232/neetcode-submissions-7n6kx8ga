"""
Optimized version 
"""

import heapq

class Twitter:

    def __init__(self):
        self.tweetData = {}   # {userId: [(timestamp, tweetId), ...]}  oldest -> newest
        self.following = {}   # {followerId: set(followeeId, ...)}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timeCounter = getattr(self, 'timeCounter', 0) + 1  # monotonic counter, not time.time()

        if userId not in self.tweetData:
            self.tweetData[userId] = []

        self.tweetData[userId].append((self.timeCounter, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        followees = self.following.get(userId, set()) | {userId}

        # seed the heap with each followee's single most recent tweet
        heap = []
        for user in followees:
            tweets = self.tweetData.get(user, [])
            if tweets:
                idx = len(tweets) - 1
                ts, tid = tweets[idx]
                heap.append((-ts, tid, user, idx))

        heapq.heapify(heap)  # size = number of followees, not number of tweets

        result = []
        while heap and len(result) < 10:
            negTs, tid, user, idx = heapq.heappop(heap)
            result.append(tid)

            idx -= 1
            if idx >= 0:
                tweets = self.tweetData[user]
                ts, nextTid = tweets[idx]
                heapq.heappush(heap, (-ts, nextTid, user, idx))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)