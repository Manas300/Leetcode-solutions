import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert to max-heap by storing negatives
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            # Pop two largest stones
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)

            if first != second:
                # Smash them, push the difference back
                heapq.heappush(max_heap, -(first - second))

        # If heap is empty → return 0, else return last stone
        return -max_heap[0] if max_heap else 0