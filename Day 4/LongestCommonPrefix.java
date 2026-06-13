class Solution {

    public String longestCommonPrefix(String[] strs) {

        // Edge case:
        // If array is null or empty,
        // no common prefix exists.
        if (strs == null || strs.length == 0) {
            return "";
        }

        // Assume first string is the common prefix
        String prefix = strs[0];

        /*
         Example:

         ["flower","flow","flight"]

         prefix = "flower"
        */

        for (int i = 1; i < strs.length; i++) {

            /*
             Check if current string starts
             with the current prefix.
            */

            while (!strs[i].startsWith(prefix)) {

                /*
                 If not,

                 Remove last character
                 from prefix.

                 flower -> flowe
                 flowe  -> flow
                 flow   -> flo
                 ...
                */

                prefix =
                    prefix.substring(
                        0,
                        prefix.length() - 1
                    );

                /*
                 If prefix becomes empty,

                 No common prefix exists.
                */

                if (prefix.isEmpty()) {
                    return "";
                }
            }
        }

        return prefix;
    }
}
