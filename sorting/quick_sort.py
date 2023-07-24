def partition(nums: list[int], left: int, right: int) -> int:
    i = left - 1
    piv = nums[right]
    for j in range(left, right):
        if nums[j] < piv:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[right] = nums[right], nums[i + 1]
    return i + 1


def quick_sort(nums: list[int]) -> list[int]:
    def _quick_sort(nums: list[int], left: int, right: int) -> None:
        if left < right:
            partition_idx = partition(nums, left, right)
            _quick_sort(nums, left, partition_idx - 1)
            _quick_sort(nums, partition_idx + 1, right)
    _quick_sort(nums, 0, len(nums) -1)
    return nums
