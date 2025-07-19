# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        sum_to_index={}
        prefix_sum=0
        max_len=0
        for i in range(len(arr)):
            prefix_sum+=arr[i]
            if prefix_sum==k:
                max_len=max(max_len,i+1)
            rem=prefix_sum-k
            if rem in sum_to_index:
                max_len=max(max_len,i-sum_to_index[prefix_sum-k])
            if prefix_sum not in sum_to_index:
                sum_to_index[prefix_sum]=i
                
        return max_len
            
        
        
        return max_len
    
