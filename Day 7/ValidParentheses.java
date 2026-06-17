class Solution {

    public boolean isValid(String s) {

        // Stack stores opening brackets
        Stack<Character> stack = new Stack<>();

        // Traverse each character
        for (char ch : s.toCharArray()) {

            /*
             If opening bracket,
             push into stack

             Example:
             (

             Stack:
             [(]
            */
            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
            }

            else {

                /*
                 Example:

                 Input:
                 )

                 If stack empty,
                 no opening bracket exists
                */
                if (stack.isEmpty()) {
                    return false;
                }

                char top = stack.pop();

                /*
                 Check matching pairs
                */

                if (ch == ')' && top != '(') {
                    return false;
                }

                if (ch == '}' && top != '{') {
                    return false;
                }

                if (ch == ']' && top != '[') {
                    return false;
                }
            }
        }

        /*
         Stack must be empty

         Example:

         Input:
         ((

         Stack:
         [(, (]

         Not empty => Invalid
        */

        return stack.isEmpty();
    }
}
