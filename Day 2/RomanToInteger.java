import java.util.*;

class Solution {
    public int romanToInt(String s) {

        HashMap<Character, Integer> map = new HashMap<>();

        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);

        int result = 0;

        for (int i = 0; i < s.length(); i++) {

            int current = map.get(s.charAt(i));

            /*
             Example:
             s = "MCMIV"

             i=0
             current = M = 1000
             next = C = 100

             1000 > 100
             Add 1000
            */

            if (i < s.length() - 1) {

                int next = map.get(s.charAt(i + 1));

                // Subtraction case
                if (current < next) {

                    /*
                     Example:
                     IV

                     I = 1
                     V = 5

                     1 < 5

                     result -= 1
                    */

                    result -= current;
                } else {

                    result += current;
                }

            } else {

                // Last character
                result += current;
            }
        }

        return result;
    }
}
