def remove_number(numbers, target):
    original_length = len(numbers)
    numbers[:] = [x for x in numbers if x != target]
    removed_count = original_length - len(numbers)
    return removed_count
nums1 = [1, 2, 3, 2, 4, 2]