class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_elem = max(nums)
        n = len(nums)
        count = 0
        left = 0
        result = 0
        
        for right in range(n):
            if nums[right] == max_elem:
                count += 1
            
            while count >= k:
                result += n - right
                if nums[left] == max_elem:
                    count -= 1
                left += 1
        
        return result