def merge_sort(nums: list[int]) -> list[int]:
    def _merge_sort(nums: list[int], left: int, right: int) -> None:
        if left < right:
            middle = (left + right) // 2
            _merge_sort(nums, left, middle)
            _merge_sort(nums, middle + 1, right)



class MergeSort:
    def __call__(nums: list[int]) -> list[int]:
        pass

    @classmethod
    def _merge_sort(nums: list[int], left: int, right: int) -> None:
        if left < right:
            
