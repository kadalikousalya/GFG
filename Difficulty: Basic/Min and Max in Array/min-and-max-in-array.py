#User function Template for python3
#User function Template for python3

class Solution:
    def get_min_max(self, arr):
        min_val=float('inf')
        max_val=float('-inf')
        for i in range(len(arr)):
            if arr[i]<min_val:
                min_val=arr[i]
            if arr[i]>max_val:
                max_val=arr[i]
        return min_val,max_val
       
    