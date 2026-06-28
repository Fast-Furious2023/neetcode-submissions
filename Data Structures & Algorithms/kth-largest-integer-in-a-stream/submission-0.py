class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.storage = sorted(nums) if nums else []
        self.pointer = k

    def add(self, val: int) -> int:
        self.storage.append(val)
        self.storage = sorted(self.storage)
        return self.storage[-self.pointer]
