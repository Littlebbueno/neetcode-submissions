import heapq

class MedianFinder:

    def __init__(self):
        self.smallHeap = [] # Vai ser a max heap
        self.largeHeap = [] # Vai ser a min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap, -1 * num) # -1 para ser uma maxHeap
        if self.smallHeap and self.largeHeap and (-1 * self.smallHeap[0]) > (self.largeHeap[0]):
            val = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)

        if len(self.smallHeap) + 1 < len(self.largeHeap):
            val = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -1 * val)
        if len(self.smallHeap) > len(self.largeHeap) + 1:
            val = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)
            

    def findMedian(self) -> float:
        if len(self.smallHeap) == len(self.largeHeap):
            median = (-1 * self.smallHeap[0] + self.largeHeap[0]) / 2
        else:
            if len(self.smallHeap) > len(self.largeHeap):
                median = -1 * self.smallHeap[0]
            else:
                median = self.largeHeap[0]
        return median
        
        