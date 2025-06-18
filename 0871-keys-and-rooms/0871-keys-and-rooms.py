class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        stack = []

        for i in rooms[0]:
            stack.append(i)
        visited.add(0)

        while stack:
            room = stack.pop()
            
            if room in visited:
                continue
            
            visited.add(room)
            
            for keys in rooms[room]:
                if keys not in visited:
                    stack.append(keys)

        return len(visited) == len(rooms)

        
        
