# 3. Longest Substring Without Repeating Characters

## Problem Statement
Given a string s, find the length of the longest substring without repeating characters.

<details> <summary>Example 1:</summary>
Input: s = "abcabcbb"

Output: 3

Explanation: The answer is "abc", with the length of 3 which is max.

</details> <details> <summary>Example 2:</summary>
Input: s = "bbbbb"

Output: 1

Explanation: The answer is "b", with the length of 1.

</details> <details> <summary>Example 3:</summary>
Input: s = "pwwkew"

Output: 3

Explanation: The answer is "wke", with the length of 3.
Note: "pwke" is a subsequence, not a substring.

</details>
Constraints:
- 0 <= s.length <= 5 * 10⁴

- s consists of English letters, digits, symbols, and spaces.

## Goal:
- Traverse the string to generate all substrings without duplicate characters.

- Use a set to store unique substrings and track the longest.

- Return the length of the longest substring with no repeating characters.

<details> <summary>Explanation:</summary>

Step 1: If the string is empty, return 0.

Step 2: For each character in the string, start a new substring.

Step 3: Use a seen set to keep track of characters in the current substring.

Step 4: If a character repeats, break the inner loop and start a new substring from the next index.

Step 5: Store each valid substring in a set to avoid duplicates.

Step 6: Find the longest substring in that set and return its length.

</details>

## The Solution:

```
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
    # Find the longest substring by length
    longest = max(substrings, key=len) if substrings else ""
    return len(longest)

input_str = "abcabcbb"
print(unique_non_repeating_substrings(input_str))  
# Output: 3
```

<center> <span style="font-size: 40px;color: #57B4BA;"> Thank you </span> </center>