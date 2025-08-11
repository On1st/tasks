def remove_number(lst, num):
    count = lst.count(num)
    lst[:] = [x for x in lst if x != num]
    return count

nums1 = [1, 2, 3, 2, 4, 2]
print(remove_number(nums1, 2), nums1)

nums2 = [5, 5, 5, 1, 2]
print(remove_number(nums2, 5), nums2)
