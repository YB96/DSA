# #11. Container With Most Water
# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# n this case, the max area of water (blue section) the container can contain is 49.
width = [1,8,6,2,5,4,8,3,7]
#width = [1,2]
area = []
for i in range(len(width)):
    for j in range(i+1,len(width)):
        #print("i an j",i+1,j)
        print("width",width[i],width[j],"distance",j-i)
        #print(min(i+1,width[j]))
        area.append(min(width[i],width[j])*(j-i))

print(max(area))