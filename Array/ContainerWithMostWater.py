def maxArea(height):
    area = 0
    left, right = 0, len(height) - 1
    while left < right:
        new_area = (right - left) * min(height[left], height[right])
        area = max(area, new_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
