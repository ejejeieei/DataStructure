class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pt1 = 0
        pt2 = 0
        len_1 = len(nums)
        sum_nums = 0
        len_min = len_1 + 1
        while(pt1 < len_1):
            sum_nums += nums[pt1]
            while(sum_nums >= target):
                len_min = min(pt1 - pt2 + 1, len_min)
                sum_nums -= nums[pt2]
                pt2 += 1
            pt1 += 1
        if len_min == len_1 + 1:
            return 0
        else:
            return  len_min