import heapq

def k_largest(nums, k):
    return heapq.nlargest(k, nums)
