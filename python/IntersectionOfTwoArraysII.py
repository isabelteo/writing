class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictionary_nums1 = {}
        # keeps track of the counts of distinct values in nums1
        for num in nums1:
            if num in dictionary_nums1:
                dictionary_nums1[num] += 1
            else:
                dictionary_nums1[num] = 1

        result = []

        for num in nums2:
            # match with nums1
            if num in dictionary_nums1 and dictionary_nums1[num] > 0:
                result.append(num)
                dictionary_nums1[num] -= 1
            else:
                continue

        return result