class Solution {
    public int maxArea(int[] height) {

        // Left pointer starts from beginning
        int left = 0;

        // Right pointer starts from end
        int right = height.length - 1;

        // Stores maximum area found so far
        int maxArea = 0;

        while (left < right) {

            /*
             Width between lines

             Example:
             left = 1
             right = 8

             width = 7
            */

            int width = right - left;

            /*
             Water height is determined by
             the shorter line

             Example:
             height[left] = 8
             height[right] = 7

             waterHeight = 7
            */

            int waterHeight =
                    Math.min(height[left], height[right]);

            /*
             Area = width × waterHeight
            */

            int currArea = width * waterHeight;

            /*
             Update maximum area
            */

            maxArea = Math.max(maxArea, currArea);

            /*
             Move the smaller height

             Reason:
             Area is limited by smaller height.

             Moving larger height won't help.
             We need a taller smaller side.
            */

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }
}
