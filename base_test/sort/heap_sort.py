# -*- coding:utf-8 -*-

"""
    堆排序
    通过二叉堆的插入删除自我调整等特性，构建最大堆和最小堆。
    最大堆实现从小到大排序
    最小堆实现从大到小排序
"""


class HeapSort:
    def sort_asc(self, arr):
        for i in range(len(arr) - 2 // 2, -1, -1):
            self.down_adjust(arr, i, len(arr))

        for i in range(len(arr) - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.down_adjust(arr, 0, i)
        return arr

    @staticmethod
    def down_adjust(arr, parent_index, length):
        temp = arr[parent_index]
        child_index = 2 * parent_index + 1
        while child_index < length:
            if child_index + 1 < length and arr[child_index + 1] > arr[child_index]:
                child_index += 1
            if temp > arr[child_index]:
                break
            arr[parent_index] = arr[child_index]
            parent_index = child_index
            child_index = 2 * child_index + 1
        arr[parent_index] = temp

    # def sort_desc(self, arr):
    #     for i in range(len(arr) - 1, -1, -1):
    #         self.up_adjust(arr, i)
    #
    #     for i in range(len(arr) - 1, 0, -1):
    #         arr[i], arr[0] = arr[0], arr[i]
    #         self.up_adjust(arr, i)
    #     return arr
    #
    # @staticmethod
    # def up_adjust(arr, last_index):
    #     temp = arr[last_index]
    #     child_index, parent_index = last_index, (last_index - 1) // 2
    #     while child_index > 0 and temp < arr[parent_index]:
    #         arr[child_index] = arr[parent_index]
    #         child_index = parent_index
    #         parent_index = (child_index - 1) // 2
    #     arr[child_index] = temp


if __name__ == '__main__':
    a = HeapSort()
    print(a.sort_asc([2, 3, 56, 7, 31, 45]))
    # print(a.sort_desc([24, 3, 56, 7, 31, 45]))
