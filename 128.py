class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = dict()
        res = 0

        for i in nums:
            if i in dic:
                dic[i] += 1
            dic[i] = 1

        for i in nums:
            if (i in dic) and (i - 1 not in dic):
                cnt = 0
                cur = i

                while cur in dic:
                    cnt += dic[cur]
                    del dic[cur]
                    cur += 1

                res = max(res, cnt)
        
        return res

