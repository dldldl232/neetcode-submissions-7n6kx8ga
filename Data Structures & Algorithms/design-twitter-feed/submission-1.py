import time

class Twitter:

    def __init__(self):
        self.tweetData= {}
        self.following = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # {userID: [tweetId], ..}
        currTime = time.time()

        if userId not in self.tweetData:
            self.tweetData[userId] = []

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
            totalPosts.extend(self.tweetData.get(user, []))
        
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
        if followerId not in self.following:
            raise KeyError()
        
        if followeeId not in self.following[followerId]:
            raise ValueError()
        
        self.following[followerId].remove(followeeId)
        
