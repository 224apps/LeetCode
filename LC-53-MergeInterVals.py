class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda interval: interval[0])

        result = [intervals[0]]
        for currInterval in intervals:
            lastInterval = result[-1]

            #if there is an overlap
            if currInterval[0] <= lastInterval[1]:
                lastInterval[1] = max(currInterval[1], lastInterval[1])
            else:
                result.append(currInterval)
        return result