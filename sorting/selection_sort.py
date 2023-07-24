def selection_sort(nums: list[int]) -> list[int]:
    n = len(nums)
    for i in range(n):
        temp = i
        for j in range(i, n):
            if nums[j] < nums[temp]:
                temp = j
        nums[i], nums[temp] = nums[temp], nums[i]
    return nums
