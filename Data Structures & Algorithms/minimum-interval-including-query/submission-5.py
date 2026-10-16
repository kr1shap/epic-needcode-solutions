from collections import defaultdict
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        #maintain index 
        idx_to_query = defaultdict(int)
        query_to_res = defaultdict(int)
        for i in range(len(queries)):
            idx_to_query[i] = queries[i]
        queries.sort()
        pq = []
        idx = 0

        # print(intervals)
        # print(queries)
        for query in queries: 
            query_to_res[query] = 20931092348102398
            while idx < len(intervals):
                if intervals[idx][0] <= query <= intervals[idx][1] or intervals[idx][1] < query:
                    length = intervals[idx][1]-intervals[idx][0]+1
                    heapq.heappush(pq, (length, intervals[idx][1]))
                    idx+=1
                else:
                    break
            # now exhaust pq if needed
            while pq and pq[0][1] < query:
                heapq.heappop(pq)
            if not pq:
                query_to_res[query] = -1
            else:
                query_to_res[query] = pq[0][0]
        result = []
        for i in range(len(queries)):
            result.append(query_to_res[idx_to_query[i]])
        return result

        