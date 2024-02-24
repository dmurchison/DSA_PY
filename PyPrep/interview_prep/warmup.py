class Challenge:
    def non_repeating_substring(self, string) -> int:
        """
        Given a string, find the length of the longest substring without repeating characters.
        """
        # Create a dictionary to store the characters and their index
        char_index = {}
        # Initialize the start index
        start = 0
        # Initialize the max length
        max_length = 0
        # Iterate through the string
        for i in range(len(string)):
            # Check if the character is already in the dictionary
            if string[i] in char_index:
                # Update the start index to the maximum of the current start index and the index of the character + 1
                start = max(start, char_index[string[i]] + 1)
            # Update the character's index
            char_index[string[i]] = i
            # Update the max length
            max_length = max(max_length, i - start + 1)
        return max_length


    def product_array(self, nums) -> list[int]:
        # Create an array to store the final result
        final_arr = []
        # Iterate through nums
        for i in range(len(nums)):
            # Append 1 to the final array to store the product of nums
            final_arr.append(1)
            # Iterate through nums again to calculate the product of the remaining elements
            for j in range(len(nums)):
                # Check if i is not equal to j
                if i != j:
                    # Multiply the final_arr[i] by nums[j]
                    final_arr[i] *= nums[j]
        return final_arr




# Test cases
print(Challenge().non_repeating_substring('abcabcbb')) # 3
print(Challenge().non_repeating_substring('bbbbbb')) # 1
print(Challenge().non_repeating_substring('pwwkew')) # 3
print()

print(Challenge().product_array([2,5,7,4,11,1,1,3])) # [4620, 1848, 1320, 2310, 840, 9240, 9240, 3080]
print(Challenge().product_array([1,2,3,4])) # [24,12,8,6]
print(Challenge().product_array([21,-2,30,4])) # [-240,2520,-168,-1260]
