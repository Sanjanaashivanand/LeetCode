from collections import defaultdict
from itertools import combinations

class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        traffic = defaultdict(list)

        for t, u, w in sorted(zip(timestamp, username, website)):
            traffic[u].append(w)

        
        pattern_users = defaultdict(set)

        for user, sites in traffic.items():
            sequences = set(combinations(sites, 3))  
            for seq in sequences:
                pattern_users[seq].add(user)

        max_pattern = max(sorted(pattern_users), key=lambda x: len(pattern_users[x]))

        return list(max_pattern)
