class Solution {

    List<String> result = new ArrayList<>();

    String[] phone = {
            "", "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
    };

    public List<String> letterCombinations(String digits) {

        // Edge case
        if (digits == null || digits.length() == 0) {
            return result;
        }

        /*
         Start backtracking

         Example:

         digits = "23"
        */

        backtrack(
                digits,
                0,
                new StringBuilder()
        );

        return result;
    }

    private void backtrack(
            String digits,
            int index,
            StringBuilder current
    ) {

        /*
         If we've processed all digits

         Example:

         current = "ad"

         Store result
        */

        if (index == digits.length()) {

            result.add(
                    current.toString()
            );

            return;
        }

        /*
         Get letters for current digit

         Example:

         digit = '2'

         letters = "abc"
        */

        String letters =
                phone[
                    digits.charAt(index) - '0'
                ];

        for (char ch : letters.toCharArray()) {

            /*
             Choose
            */

            current.append(ch);

            /*
             Explore next digit
            */

            backtrack(
                    digits,
                    index + 1,
                    current
            );

            /*
             Undo choice

             Backtracking step
            */

            current.deleteCharAt(
                    current.length() - 1
            );
        }
    }
}
