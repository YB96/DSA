#3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.
s = "abcabcbb"
s = "pwwkew"
def unique_non_repeating_substrings(s):
    if s == "":
        return 0
    substrings = set()
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break  # Stop when a repeated character is found
            seen.add(s[j])
            substrings.add(s[i:j+1])
    substrings = sorted(substrings)
    l1 = len(max(substrings,key = len))
    return l1

# Test
input_str = "abcabcbb"
print(unique_non_repeating_substrings(input_str))


def unique_non_repeating_substrings(s):
    substrings = set()
    for i in range(len(s)):
        print(f"\nOuter loop i = {i}, starting new substring from index {i}")
        seen = set()
        for j in range(i, len(s)):
            print(f"  Inner loop j = {j}, checking character '{s[j]}'")
            if s[j] in seen:
                print(f"    '{s[j]}' is already in seen set {seen}, breaking inner loop.")
                break
            seen.add(s[j])
            current_substring = s[i:j+1]
            substrings.add(current_substring)
            print(f"    Added substring: '{current_substring}', seen set is now: {seen}")
    print("\nFinal set of unique substrings (no repeats):", substrings)
    return (substrings)

# Test
input_str = "abcabcbb"
print("\n--- Running Debug Version ---")
result = unique_non_repeating_substrings(input_str)
print("\nSorted unique substrings with no repeating characters:")
print(result)
