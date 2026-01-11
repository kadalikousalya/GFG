import heapq
import math
class Solution:
	def minimumCostPath(self, grid):
		n,m=len(grid),len(grid[0])
		directions=[(1,0),(0,1),(-1,0),(0,-1)]
		dist=[[math.inf for _ in range(m)] for _ in range(n)]
		dist[0][0]=grid[0][0]
		heap=[]
		heapq.heappush(heap,(grid[0][0],0,0))
		while heap:
		    cost,r,c=heapq.heappop(heap)
		    if cost>dist[r][c]:
		        continue
		    if r==n-1 and c==m-1:
		        return cost
		        break
		    for dr,dc in directions:
		        nr=r+dr
		        nc=c+dc
		        if nr<0 or nr>=n or nc<0 or nc>=m:
		            continue
		        new_cost=cost+grid[nr][nc]
		        if new_cost<dist[nr][nc]:
		            dist[nr][nc]=new_cost
		            heapq.heappush(heap,(new_cost,nr,nc))
	    return -1
		    
		    