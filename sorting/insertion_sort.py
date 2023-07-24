def insertion_sort(nums: list[int]) -> list[int]:
    n = len(nums)
    for i in range(1, n):
        temp = nums[i]
        j = i - 1
        while j >= 0 and temp < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = temp
    return nums
