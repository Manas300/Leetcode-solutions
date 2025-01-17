class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
            # Directions: 0 = North, 1 = East, 2 = South, 3 = West
        direction = 0
        x, y = 0, 0

        # Mapping directions to coordinate changes
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for instr in instructions:
            if instr == 'G':
                dx, dy = moves[direction]
                x, y = x + dx, y + dy
            elif instr == 'L':
                direction = (direction - 1) % 4  # Turn left
            elif instr == 'R':
                direction = (direction + 1) % 4  # Turn right

        # Check if the robot is back at the origin or not facing north
        return (x == 0 and y == 0) or (direction != 0)

        