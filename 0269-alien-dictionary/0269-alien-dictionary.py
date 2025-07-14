class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def dfs(node, curr_path):
            visited.add(node)
            curr_path.add(node)

            for next in adj[node]:
                if next not in visited:
                    if dfs(next, curr_path):
                        return True
                elif next in curr_path:
                    return True

            curr_path.remove(node)
            res.append(node)
            return False

        adj = defaultdict(set)

        # Add all characters as keys
        for word in words:
            for c in word:
                adj[c]

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""  # invalid case

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break  # Only first mismatch matters
            
        res = []
        visited = set()

        for key in adj:
            if key not in visited:
                if dfs(key, set()):
                    return ""

        return ''.join(res[::-1])