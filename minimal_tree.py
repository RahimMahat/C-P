'''
Given a sorted (increasing order) array with unique integer elements, with an algorithm to create
a binary search tree with minimal height
'''

class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def minimalTree(sArray):
    if len(sArray) == 0:
        return None
    if len(sArray) == 1:
        return BSTNode(sArray[0])
    
    mid = int(len(sArray)/2)
    left = minimalTree(sArray[:mid])
    right = minimalTree[mid+1:]
    return BSTNode(sArray[mid], left, right)

arr = [1,2,3,4,5,6,7,8,9]
minimalTree(arr)
