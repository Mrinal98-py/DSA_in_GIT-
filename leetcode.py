from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        sorted_arr = []
        i = j = 0
        
        # Only consider the first m elements of nums1 and first n elements of nums2
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                sorted_arr.append(nums1[i])
                i += 1
            else:
                sorted_arr.append(nums2[j])
                j += 1
        
        # Append any remaining elements of nums1
        while i < m:
            sorted_arr.append(nums1[i])
            i += 1
        
        # Append any remaining elements of nums2
        while j < n:
            sorted_arr.append(nums2[j])
            j += 1
        
        # Copy the sorted elements back into nums1
        # for k in range(len(sorted_arr)):
        #     nums1[k] = sorted_arr[k]

        print(sorted_arr)
        print(nums1)

# Example usage:
nums1 = [3,5,8, 0, 0, 0, 0]
m = 3
nums2 = [1, 5, 6]
n = 3

solution = Solution()
solution.merge(nums1, m, nums2, n)
# print(nums1)  # Output: [1, 3, 4, 5, 6, 12]
