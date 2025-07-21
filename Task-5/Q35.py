from collections import Counter

def find_duplicates(nums):
    count = Counter(nums)
    return [num for num, freq in count.items() if freq > 1]
