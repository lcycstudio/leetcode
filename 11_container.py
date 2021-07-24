""""
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn 
such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, 
such that the container contains the most water.

Notice that you may not slant the container.


Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Example 3:
Input: height = [4,3,2,1,4]
Output: 16

Example 4:
Input: height = [1,2,1]
Output: 2


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""


def container(height):
    # constraints:
    n = len(height)
    if n < 2 or n > 105:
        return "n must be 2 <= n <= 105."
    for item in height:
        if item < 0 or item > 104:
            return "Each item must be 0 <= item <= 104."

    container = []
    for i in range(len(height)-1):
        h = height[i]
        for j in range(i+1, len(height)):
            if height[j] == h:
                b = j - i
                container.append(b*h)
            elif height[j] < h:
                b = j - i
                container.append(b * height[j])

    result = container[0]
    for item in container:
        if result <= item:
            result = item
        
    return result



if __name__ == "__main__":
    # height = [1,8,6,2,5,4,8,3,7]
    # height = [4,3,2,1,4]
    height = [1,2,1]
    print(container(height))

