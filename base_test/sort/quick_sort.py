# -*- coding:utf-8 -*-
import random


class QuickSort:
    """ 快速排序是一种比较排序，时间复杂度为（nlogn）。
        选择一个基准元素 （pivot），将比它大的元素挪到右边，比它小的元素挪到左边。
        1、双边循环法 sort_array
        2、单边循环法 sort_array2
    """
    def sort_array(self, nums):
        """
        双边循环:
        1、取第一个元素作为基准元素pivot（可以随机取一个，并与首个元素交换位置）
        2、设置left和right两个变量，指向最左和最右两个元素
        3、当left值和right值不相等时，循环4,5,6. 当两者相等，执行7
        4、如果left指向的值小于等于pivot值且left<right，则left++。否则执行4
        5、如果right指向的值大于pivot值且left<right，则right--。否则执行5
        6、如果left小于right，则交换left值和right值
        7、交换pivot和left指向的值，并返回left值。

        """
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums, start, end):
        if not nums or start >= end:
            return
        pivot_index = self.partition(nums, start, end)
        self.quick_sort(nums, start, pivot_index - 1)
        self.quick_sort(nums, pivot_index + 1, end)

    def partition(self, nums, start_index, end_index):
        left, right = start_index, end_index
        index = random.randint(start_index, end_index)
        nums[left], nums[index] = nums[index], nums[left]
        pivot = nums[start_index]  # 基准元素
        while left != right:
            while right > left and nums[right] > pivot:
                right -= 1
            while left < right and nums[left] <= pivot:
                left += 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        nums[left], nums[start_index] = pivot, nums[left]
        return left

    def sort_array2(self, nums):
        """
        单边循环
        1、取第一个元素作为基准元素pivot（可以随机取一个，并与首个元素交换位置），并将mark指向起始位置（代表小于pivot的区域边界）
        2、从下一个元素开始遍历，将遍历到的元素与pivot对比，如果大于，就继续遍历。否则执行第3步
        3、mark++， 并将遍历到的值与mark指向的值，交换位置。此时比pivot小的值多了一个。遍历完成执行4
        4、将基准元素pivot与mark指向的值交换位置
        """
        self.quick_sort2(nums, 0, len(nums) - 1)
        return nums

    def quick_sort2(self, nums, start, end):
        if not nums or start >= end:
            return
        pivot_index = self.partition2(nums, start, end)
        self.quick_sort2(nums, start, pivot_index - 1)
        self.quick_sort2(nums, pivot_index + 1, end)

    def partition2(self, nums, start_index, end_index):
        index = random.randint(start_index, end_index)
        nums[start_index], nums[index] = nums[index], nums[start_index]
        mark, pivot = start_index, nums[start_index]
        for i in range(start_index, end_index + 1):
            if nums[i] < pivot:
                mark += 1
                nums[mark], nums[i] = nums[i], nums[mark]
        nums[start_index], nums[mark] = nums[mark], nums[start_index]
        return mark


if __name__ == '__main__':
    q = QuickSort()
    print(q.sort_array2([2,3,12,4,45,65,34]))
