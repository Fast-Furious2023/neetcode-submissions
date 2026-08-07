class TimeMap:

    def __init__(self):
        self.table = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.table:
            self.table[key]=[(timestamp,value)]
        self.table[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.table.get(key, '')
        n = len(values)
        if not values:
            return ""
        
        if timestamp < values[0][0]:
            return ""
        
        if timestamp > values[n-1][0]:
            return values[n-1][1]

        
        l,r = 0,n-1
        while l <= r:
            mid = l + (r-l)//2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid -1
        
        return values[r][1]
        
