class Solution:
    def getSecondLargest(self, arr):
        first=-1
        second=-1
        for i in range(len(arr)):
            if arr[i]>first:
                second=first
                first=arr[i]
            elif arr[i]!=first and second<arr[i]:
                second=arr[i]
        return second
    