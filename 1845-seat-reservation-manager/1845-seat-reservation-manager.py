import heapq

class SeatManager:

    def __init__(self, n: int):
        self.q = [i for i in range(1, n+1)]
        heapq.heapify(self.q)
        
    def reserve(self) -> int:
        number = heapq.heappop(self.q)
        return number

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.q, seatNumber)
        
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)