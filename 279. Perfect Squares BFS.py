from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0

        dist = [-1] * (n+1)
        dist[0] = 0
        q = deque([0])

        while q:
            curr = q.popleft()
            if curr == n:
                return dist[curr]

            j = 1
            while curr + j**2 <= n:
                nxt = curr + j**2
                if dist[nxt] == -1:
                    dist[nxt] = dist[curr] + 1
                    q.append(nxt)
                j += 1
        return -1
sol = Solution()
print(sol.numSquares(12))
