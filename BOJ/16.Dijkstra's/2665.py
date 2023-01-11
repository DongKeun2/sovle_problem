# 미로만들기
# 33060KB, 44ms

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# 0,0에서 시작
def sol():
    q = []
    heappush(q, (0, 0, 0))
    while q:
        num, si, sj = heappop(q)
        for d in range(4):
            ei = si + di[d]
            ej = sj + dj[d]
            if 0 <= ei < N and 0 <= ej < N:
                # 하얀방은 +0
                if arr[ei][ej] == '1' and tmp[ei][ej] > num:
                    tmp[ei][ej] = num
                    heappush(q, (num, ei, ej))
                # 검은방은 + 1 
                if arr[ei][ej] == '0' and tmp[ei][ej] > num + 1:
                    tmp[ei][ej] = num + 1
                    heappush(q, (num+1, ei, ej))


N = int(input())
arr = [list(input()) for _ in range(N)]

tmp = [[N*N]*N for _ in range(N)]
tmp[0][0] = 0
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
sol()

print(tmp[N-1][N-1])