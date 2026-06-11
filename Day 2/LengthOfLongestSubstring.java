class Solution {
    public int lengthOfLongestSubstring(String s) {

        HashSet<Character> set = new HashSet<>();

        int left = 0;      // Start of window
        int maxLen = 0;    // Stores maximum length found

        for (int right = 0; right < s.length(); right++) {

            char currentChar = s.charAt(right);

            // If character already exists in window,
            // shrink window from left until duplicate is removed
            while (set.contains(currentChar)) {

                /*
                Example for "abcabcbb"

                Window = [a,b,c]
                right points to second 'a'

                Since 'a' already exists:
                remove s[left] = 'a'
                left++

                Window becomes [b,c]
                */

                set.remove(s.charAt(left));
                left++;
            }

            // Add current character into window
            set.add(currentChar);

            /*
            Dry Run for "abcabcbb"

            right=0, char='a'
            set = [a]
            window = "a"
            length = 1
            maxLen = 1

            right=1, char='b'
            set = [a,b]
            window = "ab"
            length = 2
            maxLen = 2

            right=2, char='c'
            set = [a,b,c]
            window = "abc"
            length = 3
            maxLen = 3

            right=3, char='a'
            duplicate found

            remove 'a'
            left becomes 1

            add current 'a'

            set = [b,c,a]
            window = "bca"
            length = 3
            maxLen = 3

            right=4, char='b'
            duplicate found

            remove 'b'
            left becomes 2

            add current 'b'

            window = "cab"
            length = 3
            maxLen = 3
            */

            int currentLength = right - left + 1;

            maxLen = Math.max(maxLen, currentLength);
        }

        return maxLen;
    }
}
