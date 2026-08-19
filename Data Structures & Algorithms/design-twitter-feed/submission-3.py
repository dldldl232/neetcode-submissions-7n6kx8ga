import time
"""
time.time() is risky: under fast successive calls two postTweets can get the same timestamp. much safer pattern: use a global monotonic counter (itertools.count()) instead of real time. It guarantees strict ordering, has zero collision risk, and is cheaper than a syscall on every post.
"""

class Twitter:

    def __init__(self):
        self.tweetData= {}
        self.following = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # {userID: [tweetId], ..}
        currTime = time.time()

        if userId not in self.tweetData:
            self.tweetData[userId] = []

        """user's own tweet list is in chronological order"""
        self.tweetData[userId].append((currTime, tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        # fetch tweetId from users that the user is following or the user themselves
        # fetches at most 10 tweetId
        # tweetId has to be ordered from most recent to least recent
        totalPosts = []
        
        # extract all related users
        followees = self.following.get(userId, set()) | {userId}
        
        # extract the posts from each users and put into totalPosts
        for user in followees:
            """totalPosts.extend(self.tweetData.get(user, []))""" 
            totalPosts.extend(self.tweetData.get(user, [])[-10:]) # this is more efficient than the prev line
        
        # we compare and return at most 10 recent posts
        heapq.heapify_max(totalPosts)

        output = [heapq.heappop_max(totalPosts)[1] for _ in range(min(10, len(totalPosts)))]

        return output


    def follow(self, followerId: int, followeeId: int) -> None:
        #{followerId: [followeeId], ..}
        if followerId not in self.following:
            self.following[followerId] = set()
        
        self.following[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        # if followerId not in self.following:
        #     raise KeyError()
        
        # if followeeId not in self.following[followerId]:
        #     raise ValueError()
        
        if followerId in self.following:
            self.following[followerId].discard(followeeId)

            # .remove raises keyerrors for missing elements
            # while .discard does nothing if it does not exist        
