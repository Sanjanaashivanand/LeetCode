class Solution(object):
    
    def predictPartyVictory(self, senate):
        q = []
        radiants = 0
        dire = 0

        for i in senate:
            q.append(i)
            if i == "R":
                radiants += 1
            else:
                dire += 1

        n = len(q)
        i = 0

        while radiants > 0 and dire > 0:
            if q[i] == -1:
                i = (i + 1) % len(q)
                continue

            # Find next opponent to ban
            j = (i + 1) % len(q)
            while q[j] == -1 or q[j] == q[i]:
                j = (j + 1) % len(q)
                if j == i:  # No one left to ban
                    break

            # If everyone else is same party, declare win
            if q[j] == q[i] or j == i:
                return "Radiant" if q[i] == "R" else "Dire"

            # Ban opponent
            if q[j] == "R":
                radiants -= 1
            else:
                dire -= 1
            q[j] = -1  # mark as banned

            # Move to next senator
            i = (i + 1) % len(q)

        return "Radiant" if radiants > 0 else "Dire"
