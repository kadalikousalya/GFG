# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def deleteNode(head, x):
    # Code here
    if head is None:
        return None
    if x==1:
        return head.next
    temp=head
    count=1
    while temp is not None and count<x-1:
        temp=temp.next
        count+=1
    while temp is None or temp.next is None:
        return None
    temp.next=temp.next.next
    return head