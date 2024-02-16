# Definition for singly-linked list.
import heapq


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        heap = []
        for i in lists:
            if i is not None:
                heapq.heappush(heap, (i.val, i))

        prehead = ListNode(-1)
        head = prehead
        while len(heap) > 0:
            _, l = heapq.heappop(heap)
            if l.val is not None:
                head.next = l
                head = head.next
                l = l.next
                if l is not None:
                    heapq.heappush(heap, (l.val, l))

        return prehead.next

    # create a heap with value and linkedlist in the heap
    # first add all the list in the heap
    # the run a while loop until heap is empty
    # pop the smallest value from head add it to answer and add that next value of that list into heap again
    # at the end return new linkedlist

    #     merged_list = ListNode(-1)
    #     p1 = merged_list
    #     min_value_index = self.find_min_value_list(lists)
    #     while min_value_index is not None:
    #         p1.next = lists[min_value_index]
    #         p1 = p1.next
    #         lists[min_value_index] = lists[min_value_index].next
    #         min_value_index = self.find_min_value_list(lists)
    #     return merged_list.next

    # def find_min_value_list(self,lists):

    #     min_value_index = None
    #     min_val = None
    #     for ind, list_ in enumerate(lists):
    #         if list_ is not None:
    #             if  min_value_index is None or list_.val < min_val:
    #                 min_val = list_.val
    #                 min_value_index = ind
    # return min_value_index


# start a merged_list with a node -1 value
# find the min accross all the lists
# a seprate function which gives the min value in from all the lists
# here we have to ignore null value linked lists
# the return of the function would be the linked list itselt and the updated lists list
# we will do this by using index
# if there are no more values in all lists then we will just return nuone in min value
#                   [[1,4,5],[1,3,4],[2,6]]
# min_value_index                     0
# min_val                             1
# to make better time complexity merge two lists at a time and it will work like merge sort algorithm
