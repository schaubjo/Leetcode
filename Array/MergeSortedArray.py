def merge(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    back = m + n - 1

    while back >= 0:
        if p1 < 0:
            nums1[back] = nums2[p2]
            p2 -= 1
        elif p2 < 0:
            nums1[back] = nums1[p1]
            p1 -= 1
        elif nums1[p1] > nums2[p2]:
            nums1[back] = nums1[p1]
            p1 -= 1
        else:
            nums1[back] = nums2[p2]
            p2 -= 1

        back -= 1

    print(nums1)


merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
