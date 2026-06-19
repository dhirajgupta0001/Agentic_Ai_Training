class Solution {

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        // Dummy node to simplify list creation
        ListNode dummy = new ListNode(0);

        // Pointer used to build merged list
        ListNode current = dummy;

        /*
         Example:

         list1 = 1 -> 2 -> 4
         list2 = 1 -> 3 -> 4
        */

        while (list1 != null && list2 != null) {

            /*
             Compare current nodes
            */

            if (list1.val <= list2.val) {

                /*
                 Example:

                 1 <= 1

                 Take node from list1
                */

                current.next = list1;

                // Move list1 forward
                list1 = list1.next;

            } else {

                /*
                 Take node from list2
                */

                current.next = list2;

                // Move list2 forward
                list2 = list2.next;
            }

            // Move current pointer forward
            current = current.next;
        }

        /*
         One list may still have nodes left

         Attach remaining nodes directly
        */

        if (list1 != null) {
            current.next = list1;
        } else {
            current.next = list2;
        }

        // Return merged list
        return dummy.next;
    }
}
