class Solution(object):
    def findWinningPlayer(self, skills, k):
        """
        :type skills: List[int]
        :type k: int
        :rtype: int
        """
        n = len(skills)
        win_streak = 0
        max_player = skills[0]
        index = 0

        for i in range(1, n):
            if skills[i] > max_player:
                max_player = skills[i]
                index = i
                win_streak = 1
            else:
                win_streak += 1

            if win_streak == k:
                return index

        return index 
