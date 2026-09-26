
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, num in enumerate(nums):
            required = target - num

            if required in hash_map:
                return [hash_map[required], index]

            hash_map[num] = index