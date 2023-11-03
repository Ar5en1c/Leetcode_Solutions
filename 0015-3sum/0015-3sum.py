class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        res = []

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = nums[i]

            while l < r:
                summ = target + nums[l] + nums[r]
                if summ == 0:
                    res.append([target, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif summ > 0:
                    r -= 1
                elif summ < 0:
                    l += 1
                
        return res