class Twitter {
    private Map<Integer, List<Tweet>> userTweets;
    private Map<Integer, Set<Integer>> followers;
    private int timestamp;

    public Twitter() {
        userTweets = new HashMap<>();
        followers = new HashMap<>();
        timestamp = 0;
    }

    public void postTweet(int userId, int tweetId) {
        Tweet tweet = new Tweet(tweetId, timestamp++);
        if(!userTweets.containsKey(userId)) userTweets.put(userId,new ArrayList<>());
        userTweets.get(userId).add(tweet);
        //userTweets.computeIfAbsent(userId, k -> new ArrayList<>()).add(tweet);
    }

    public List<Integer> getNewsFeed(int userId) {
        Set<Integer> followedUsers = new HashSet<>(followers.getOrDefault(userId, new HashSet<>()));
        followedUsers.add(userId);  // User sees their own tweets

        PriorityQueue<Tweet> pq = new PriorityQueue<>((a, b) -> b.timestamp - a.timestamp);
        for (int followedUser : followedUsers) {
            List<Tweet> tweets = userTweets.get(followedUser);
            if (tweets != null) {
                pq.addAll(tweets);
            }
        }

        List<Integer> newsFeed = new ArrayList<>();
        while (!pq.isEmpty() && newsFeed.size() < 10) {
            newsFeed.add(pq.poll().tweetId);
        }

        return newsFeed;
    }

    public void follow(int followerId, int followeeId) {
        if(!followers.containsKey(followerId))followers.put(followerId,new HashSet<>());
        followers.get(followerId).add(followeeId);
        //followers.computeIfAbsent(followerId, k -> new HashSet<>()).add(followeeId);
    }

    public void unfollow(int followerId, int followeeId) {
        Set<Integer> userFollowers = followers.get(followerId);
        if (userFollowers != null) {
            userFollowers.remove(followeeId);
        }
    }

    private static class Tweet {
        int tweetId;
        int timestamp;

        Tweet(int tweetId, int timestamp) {
            this.tweetId = tweetId;
            this.timestamp = timestamp;
        }
    }
}