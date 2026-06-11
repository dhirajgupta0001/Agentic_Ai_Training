class Solution {

    public String longestPalindrome(String s) {

        // If string is empty or has only one character,
        // it is already a palindrome.
        if (s == null || s.length() < 2) {
            return s;
        }

        // These will store the starting and ending index
        // of the longest palindrome found.
        int start = 0;
        int end = 0;

        /*
         Example Input:

         s = "babad"

         Index:
         0 1 2 3 4
         b a b a d
        */

        for (int i = 0; i < s.length(); i++) {

            /*
             Check ODD length palindrome

             Example:
             "bab"

             b a b
               ^
             center = 'a'

             left = i
             right = i
            */
            int len1 = expandFromCenter(s, i, i);

            /*
             Check EVEN length palindrome

             Example:
             "abba"

             a b b a
               | |
             center between b and b

             left = i
             right = i + 1
            */
            int len2 = expandFromCenter(s, i, i + 1);

            // Take whichever palindrome is larger
            int maxLen = Math.max(len1, len2);

            /*
             Example for "babad"

             When i = 1

             b a b a d
               ^

             expand => "bab"

             len1 = 3
             len2 = 0

             maxLen = 3
            */

            if (maxLen > end - start) {

                /*
                 Calculate actual start and end indices

                 Example:

                 palindrome = "bab"
                 center = 1
                 length = 3

                 start = 1 - (3-1)/2
                       = 0

                 end = 1 + 3/2
                     = 2

                 substring(0,2) => "bab"
                */

                start = i - (maxLen - 1) / 2;
                end = i + maxLen / 2;
            }
        }

        /*
         Example:

         start = 0
         end = 2

         s.substring(0,3)

         => "bab"
        */
        return s.substring(start, end + 1);
    }

    private int expandFromCenter(String s, int left, int right) {

        /*
         Example:

         s = "babad"

         Call:

         expandFromCenter(s,1,1)

         left = 1
         right = 1

         b a b a d
           L
           R
        */

        while (
                left >= 0 &&
                right < s.length() &&
                s.charAt(left) == s.charAt(right)
        ) {

            /*
             First Iteration

             a == a

             Expand

             left = 0
             right = 2

             b a b a d
             L   R
            */

            /*
             Second Iteration

             b == b

             Expand

             left = -1
             right = 3
            */

            left--;
            right++;
        }

        /*
         Loop stopped because:

         left = -1
         right = 3

         Current palindrome is:

         b a b

         Length formula:

         right - left - 1

         = 3 - (-1) - 1

         = 3
        */

        return right - left - 1;
    }
}
