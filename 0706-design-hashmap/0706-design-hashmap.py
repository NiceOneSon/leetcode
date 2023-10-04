class MyHashMap:

    def __init__(self):
        self.routes = [None] * (10**6 + 1)

    def put(self, key: int, value: int) -> None:
        self.routes[key] = value

    def get(self, key: int) -> int:
        if self.routes[key] == None:
            return -1
        return self.routes[key]
        

    def remove(self, key: int) -> None:
        self.routes[key] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)