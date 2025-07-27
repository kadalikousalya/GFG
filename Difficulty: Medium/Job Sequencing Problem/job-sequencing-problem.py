class Solution:
    def find(self, parent, i):
        # Find with path compression
        if parent[i] == i:
            return i
        parent[i] = self.find(parent, parent[i])
        return parent[i]

    def jobSequencing(self, deadline, profit):
        # code here
        jobs=list(zip(deadline,profit))
        jobs.sort(key=lambda x:x[1],reverse=True)
        max_deadline=max(deadline)
        parent = [i for i in range(max_deadline + 1)]
        total_profit=0
        count_jobs=0
        for d,p in jobs:
            available_slot = self.find(parent, d)
            if available_slot > 0:
                parent[available_slot] = self.find(parent, available_slot - 1)
                total_profit+=p
                count_jobs+=1
                
        return count_jobs,total_profit