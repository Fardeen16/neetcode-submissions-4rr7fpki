class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        dictt = {}
        for n in hand:
            dictt[n] = 1 + dictt.get(n, 0)

        min_heap = list(dictt.keys())
        heapq.heapify(min_heap)

        while min_heap:
            # check for the top number if hand is possible
            card = min_heap[0]
            for i in range(card, card + groupSize):
                if i not in dictt:
                    return False
                dictt[i] -= 1

            # pop from heap if count = 0 
                if dictt[i] == 0:
                    if min_heap[0] != i:
                        return False
                    heapq.heappop(min_heap)
        return True
        