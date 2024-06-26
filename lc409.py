class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Create a dictionary to count the occurrences of each character
        char_count = {}

        # Count each character in the input string
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        longest_palindrome = 0
        odd_found = False

        # Calculate the length of the longest palindrome
        for count in char_count.values():
            if count % 2 == 0:
                longest_palindrome += count
            else:
                longest_palindrome += count - 1
                odd_found = True

        # If there was at least one character with an odd count, add 1 to the result
        if odd_found:
            longest_palindrome += 1

        return longest_palindrome

if __name__ == "__main__" :
    print(Solution().longestPalindrome("test"))
