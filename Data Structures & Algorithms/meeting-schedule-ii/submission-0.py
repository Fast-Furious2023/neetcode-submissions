"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #verify input for empty input
        if not intervals:
            return 0

        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        start_index = 0
        end_index = 0

        rooms = 0
        max_rooms = 0

        while start_index < len(starts):
            if starts[start_index] >= ends[end_index]:
                rooms -= 1
                end_index += 1

            rooms += 1
            start_index += 1

            max_rooms=max(max_rooms, rooms)

        return max_rooms
        