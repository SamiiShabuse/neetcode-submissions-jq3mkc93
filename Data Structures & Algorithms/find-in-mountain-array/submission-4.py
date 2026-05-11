class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        len = mountainArr.length()
        cache = {}

        def get(i):
            if i not in cache:
                cache[i] = mountainArr.get(i)
            return cache[i]
        

        # find the peak
        l, r = 1, len - 2
        while l <= r:
            m = (l + r) // 2
            lft, mid, rgt = get(m-1), get(m), get(m+1)
            if lft < mid < rgt:
                l = m + 1
            elif lft > mid > rgt:
                r = m - 1
            else:
                break
        

        peak = m 

        def binary_search(l, r, ascending):
            while l <= r:
                m = (l + r) // 2
                val = get(m)
                if val == target:
                    return m 
                if ascending == (val < target):
                    l = m + 1
                else:
                    r = m - 1
            return - 1

        # search left
        res = binary_search(0, peak, True)
        if res != -1:
            return res

        # search right
        return binary_search(peak, len - 1, False)