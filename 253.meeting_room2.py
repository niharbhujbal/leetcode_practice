from collections import defaultdict
import heapq


class Solution:
    def minMeetingRooms(self, intervals):

        intervals.sort(key=lambda x: (x[0], x[1] - x[0]))

        heap = []
        room_no = 0

        for interval in intervals:
            rn = room_no
            # if len(heap) == 0:
            # heapq.heappush(heap,(interval[-1], room_no))

            # which room is gonna be empty first that rooms ending time is less than
            if len(heap) > 0 and heap[0][0] <= interval[0]:
                max_time, rn = heapq.heappop(heap)
                # heapq.heappush(heap,(interval[-1],rn))
            else:
                room_no += 1
            heapq.heappush(heap, (interval[-1], room_no))

        return room_no


class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x: x[0])

        meetingrooms = defaultdict(list)
        breakv = False
        for i in intervals:
            for j in range(len(meetingrooms)):
                if meetingrooms[j][-1][-1] <= i[0]:
                    meetingrooms[j].append(i)
                    breakv = True
                    break
            if not breakv:

                meetingrooms[len(meetingrooms)].append(i)
            breakv = False
        return max(meetingrooms.keys()) + 1
