class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)
        
        # Max-heap of (-freq, char)
        pq = [(-count, char) for char, count in freq.items()]
        heapq.heapify(pq)

        prev = (0, '')  # (prev_freq, prev_char)
        res = []

        while pq:
            curr_freq, curr_char = heapq.heappop(pq)
            res.append(curr_char)

            # Push back the previous character if it still has remaining count
            if prev[0] < 0:
                heapq.heappush(pq, prev)

            # Update previous to be current, with one fewer count
            prev = (curr_freq + 1, curr_char)  # Adding 1 because frequencies are negative

        result = ''.join(res)

        # Final validation: no adjacent characters should be the same
        if len(result)!=len(s):
            return ""

        return result