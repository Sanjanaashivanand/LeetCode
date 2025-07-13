from collections import deque

class SnakeGame(object):

    def __init__(self, width, height, food):
        self.width = width
        self.height = height
        self.food = deque(food)

        self.snake = set()
        self.trail = deque()
        self.head = (0, 0)

        self.trail.append(self.head)
        self.snake.add(self.head)

        self.directions = {
            "U": (-1, 0),
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1)
        }

    def move(self, direction):
        dr, dc = self.directions[direction]
        r, c = self.head
        new_head = (r + dr, c + dc)

        # 1. Boundary check
        if not (0 <= new_head[0] < self.height and 0 <= new_head[1] < self.width):
            return -1

        # 2. Self-collision check (except tail, which is about to move)
        tail = self.trail[0]
        if new_head in self.snake and new_head != tail:
            return -1

        # 3. Eat food or move
        if self.food and self.food[0] == list(new_head):
            self.food.popleft()
            # Don't remove tail — snake grows
        else:
            removed = self.trail.popleft()
            self.snake.remove(removed)

        self.trail.append(new_head)
        self.snake.add(new_head)
        self.head = new_head

        return len(self.trail) - 1  # score = snake length - 1
