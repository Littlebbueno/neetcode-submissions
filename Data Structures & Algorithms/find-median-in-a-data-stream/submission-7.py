import heapq

class MedianFinder:
    

    def __init__(self):
        self.smallHeap = [] # MaxHeap
        self.largeHeap = [] # MinHeap (Normal)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap, -1 * num)
        if self.largeHeap and self.smallHeap:
            if -1 * self.smallHeap[0] > self.largeHeap[0]:
                val = -1 * heapq.heappop(self.smallHeap)
                heapq.heappush(self.largeHeap, val)
            if len(self.smallHeap) > len(self.largeHeap) + 1:
                val = -1 * heapq.heappop(self.smallHeap)
                heapq.heappush(self.largeHeap, val)
            if len(self.largeHeap) > len(self.smallHeap) + 1:
                val = heapq.heappop(self.largeHeap)
                heapq.heappush(self.smallHeap, -1 * val)
        if not self.largeHeap:
            val = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)

    def findMedian(self) -> float:
        if len(self.smallHeap) == len(self.largeHeap):
            val1 = -1 * self.smallHeap[0]
            val2 = self.largeHeap[0]
            return (val1 + val2) / 2
        else:
            if len(self.smallHeap) > len(self.largeHeap):
                return -1 * self.smallHeap[0]
            if len(self.smallHeap) < len(self.largeHeap):
                return self.largeHeap[0]
        
        