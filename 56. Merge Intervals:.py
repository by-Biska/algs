from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        prev_start = intervals[0][0]
        prev_finish = intervals[0][1]
        result = [[prev_start, prev_finish]]
        for i in range(1, len(intervals)):
            
            prev_start = result[-1][0]
            prev_finish = result[-1][1]
            

            cur_start = intervals[i][0]
            cur_finish = intervals[i][1]

            if cur_start <= prev_finish and cur_finish <= prev_finish:
                pass
            elif cur_start <= prev_finish:
                result[-1] = [result[-1][0], cur_finish]
            elif cur_start > prev_finish:
                result.append([cur_start, cur_finish])
        
        return result
solution = Solution()
intervals = [[2,3],[4,5],[6,7],[8,9], [2, 6]]
result = solution.merge(intervals)
print(f"Результат для {intervals}: {result}")