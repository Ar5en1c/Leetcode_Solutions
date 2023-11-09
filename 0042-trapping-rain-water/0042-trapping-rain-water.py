class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        lMax = height[l]
        rMax = height[r]
        water = 0

        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(height[l],lMax)
                water += lMax - height[l]
            else:
                r -= 1
                rMax = max(height[r],rMax)
                water += rMax - height[r]

        return water
