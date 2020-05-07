# -*- coding:utf-8 -*-

"""
    计数排序：
    取给定数组中的最大值和最小值，构建两者差长度的数组。将两个最值映射到数组的首尾两个节点，然后其他值减去最小值后得到在该数组中的位置，
    然后将其塞入数组中。 稳定排序
    局限性：
        1、当最大值和最小值差别过大，浪费空间和时间
        2、当数列中的元素为小数时，难度过大
"""


class CountSort:

    @staticmethod
    def count_sort(arr):
        l, r = min(arr), max(arr)
        temp_arr = [0] * (r - l + 1)
        for i in arr:
            temp_arr[i - l] += 1
        for index, item in enumerate(temp_arr):
            if index == 0:
                continue
            temp_arr[index] = temp_arr[index] + temp_arr[index - 1]

        result = [0] * len(arr)
        for index, item in enumerate(temp_arr):
            if index == 0:
                result[index: item] = [index + l] * item
            else:
                last_item = temp_arr[index - 1]
                if item == last_item:  # 当前节点无数据
                    continue
                else:
                    result[last_item: item] = [index + l] * (item - last_item)
        return result

    @staticmethod
    def count_sort2(arr):
        min_data, r = min(arr), max(arr)
        temp_arr = [0] * (r - min_data + 1)
        for i in arr:
            temp_arr[i - min_data] += 1
        for index, item in enumerate(temp_arr):
            if index == 0:
                continue
            temp_arr[index] = temp_arr[index] + temp_arr[index - 1]

        result = [0] * len(arr)
        for i in arr[::-1]:
            result[temp_arr[i - min_data] - 1] = i
            temp_arr[i - min_data] -= 1
        return result


if __name__ == '__main__':
    c = CountSort()
    print(c.count_sort2([6, 8, 29, 34, 45, 34]))
