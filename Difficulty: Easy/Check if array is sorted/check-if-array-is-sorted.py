class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        i=0
        j=1
        while j<len(arr):
            if arr[i]>arr[j]:
                return False
            i+=1
            j+=1
        return True