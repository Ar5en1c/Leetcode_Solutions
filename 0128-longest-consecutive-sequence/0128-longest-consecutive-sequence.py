class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        seq = 0

        for i in nums:
            if (i - 1) not in numset:
                temp_seq = 1
                while i + temp_seq in numset:
                    temp_seq += 1
                seq = max(seq, temp_seq)
        return seq