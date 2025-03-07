# 11. Container With Most Water
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. in this case, the max area of water (blue section) the container can contain is 49.

## Goal:</br>
You're trying to find the maximum area that can be formed between two lines, where the lines are represented by the width array. The area between two lines is calculated by the formula:

Area = min(height[left] , height[right]) × (right − left)
 </br>

* Here, height[left] and height[right] represent the height of the lines at positions left and right
* The distance between the lines is simply right - left.

<details>
    <summary> How the Two-Pointer Approach Works: </summary>

* We start with two pointers, left at the beginning (index 0) and right at the end (index len(width) - 1)
* The idea is to calculate the area between the lines at these two positions (left and right).
* Then, we move one of the pointers inward (either increase left or decrease right) based on a key observation: the area is limited by the shorter line, so we should try to move the pointer that is pointing to the shorter line
* This gives us the possibility of finding a taller line, which might form a larger area with the remaining line
</details>

<details>
    <summary> Why not just move both pointers one step each time? </summary>

* If you always move both pointers inward, you'll miss the opportunity to potentially find a larger area. This is because the area is constrained by the shorter of the two lines
* If you move the taller line's pointer, you don't change the limiting factor (the shorter line), so the area can't increase
</details>

<details>
    <summary> Why move the shorter line? </summary>

* The area between two lines is calculated as the minimum height of the two lines multiplied by the distance between them. 
* If the shorter line remains fixed, moving the other pointer inward will reduce the distance but not necessarily increase the height. 
* However, if we move the pointer at the shorter line, we increase the chances of encountering a taller line, which could increase the area.
</details>

## The Solution:
```
# Example
width = [1, 8, 6, 2, 5, 4, 8, 3, 7]  
left, right = 0, len(width) - 1
max_area = 0  # To store the maximum area

while left < right:
    # Calculate the current area between the two lines
    current_area = min(width[left], width[right]) * (right - left)
    
    # We will be updating max_area if the current_area is larger
    max_area = max(max_area, current_area)
    
    # Move the pointer pointing to the shorter line
    if width[left] < width[right]:
        left += 1
    else:
        right -= 1

print(max_area)  
```