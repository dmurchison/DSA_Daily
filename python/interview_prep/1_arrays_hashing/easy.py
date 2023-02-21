from typing import List


# EASY PROBLEMS
class Solution:
    def contains_duplicate(self, nums: list) -> list:
        mySet = ()
        for i in nums:
            for i in mySet:
                return True
            return False



# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice 
# in the array, and return false if every element is distinct.

class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        # Create an empty set, a set is basically a dictionary without values.
        # The rule of not having any duplicates still applies.
        mySet = set()
        # Iterate through the nums array.
        for i in nums:
            # Check if the set contains the number already.
            if i in mySet:
                # Once the set has a duplicate we exit the function by returning True.
                return True
            # Still iterating through nums; add each iterable to the set.
            mySet.add(i)
        # If the loop finishes without returning true, we know there were no duplicates.
        return False


print(Solution().contains_duplicate([1,2,3,1])) # True
print(Solution().contains_duplicate([1,2,3,4])) # False
print(Solution().contains_duplicate([1,1,1,3,3,4,3,2,4,2])) # True
print(Solution().contains_duplicate([1,2,3,4,5,6,7,8,9,10])) # False
print(Solution().contains_duplicate([1,1,1,1,1,1,1,1,1,1])) # True
print(Solution().contains_duplicate([1,1,2,2])) # True
print()



# Valid Anagram
# Given two strings s and t , write a function to determine if t is an anagram
# of s.

class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        # First check if s and t strings are the same length.
        if len(s) != len(t):
            return False
        # Create two hashes to represent each string.
        hashS, hashT = {}, {}

        # Add values to the hashes by iterating through the length of the strings
        # and incrementing the values by 1.
        for i in range(len(s)):
            # Set the value of the current key to 1 + the original value of that key
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)
        # Now that we have two hash_counters representing each string, return this boolean.
        return hashS == hashT


print(Solution().is_anagram("anagram", "nagaram")) # True
print(Solution().is_anagram("rat", "car")) # False
print(Solution().is_anagram("a", "ab")) # False
print(Solution().is_anagram("ab", "a")) # False
print(Solution().is_anagram("aacc", "ccac")) # False
print(Solution().is_anagram("racecar", "racecar")) # True
print()



# Replace Elements with Greatest Element on Right Side
# Given an array arr, replace every element in that array with the greatest 
# element among the elements to its right, and replace the last element with -1.
# After doing so, return the array.

class Solution:
    def right_side_list(self, nums: List[int]) -> List[int]:
        # Set -1 to a variable to be used during the iteration.
        rightMax = -1
        # Iterate backwards through the nums array.
        for i in range(len(nums) - 1, -1, -1):
            # Max of nums[i] and the current rightMax gets saved to newMax var.
            newMax = max(rightMax, nums[i])
            # Replace nums[i] with the highest value to the right.
            nums[i] = rightMax
            # Set the new rightMax to be the result of the last number and start the loop over.
            rightMax = newMax
        return nums


print(Solution().right_side_list([1,12,3,5,-5,2])) # [12,5,5,2,2,-1]
print(Solution().right_side_list([8,5,10,22,-14,12,5,8])) # [22,22,22,12,12,8,8,-1]
