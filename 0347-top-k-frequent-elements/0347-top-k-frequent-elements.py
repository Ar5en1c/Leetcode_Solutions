class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums

        dicT = {}
        for i in range(len(nums)):
            dicT[nums[i]] = 1 + dicT.get(nums[i], 0)

        sorted_dicT = sorted(dicT.items(), key=lambda x:x[1], reverse = True)

        i=0
        res = []

        while i < k:
            res.append(sorted_dicT[i][0])
            i += 1
        
        return res
