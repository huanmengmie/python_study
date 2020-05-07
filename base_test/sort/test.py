# -*- coding:utf-8 -*-

class Solution:
    def movingCount(self, m, n, k) -> int:
        num = 0
        for i in range(m):
            for j in range(n):
                if sum(map(lambda a: int(a), ''.join([str(i), str(j)]))) <= k:
                    print((i, j))
                    num += 1
                else:
                    break
        return num


if __name__ == '__main__':
    s = Solution()
    print(s.movingCount(16, 8, 4))
    print(s.movingCount(38, 15, 9))
