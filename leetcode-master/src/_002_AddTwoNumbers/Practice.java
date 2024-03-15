
package _002_AddTwoNumbers;

import com.leetcode.ListNode;

public class Practice {

    public ListNode addTwoNumbers(ListNode a, ListNode b) {
        // Create two sum lists
        ListNode sumHead1 = new ListNode(0);
        ListNode sumHead2 = new ListNode(0);
        ListNode current1 = a;
        ListNode current2 = b;
        ListNode currentSum = sumHead1;

        // Iterate over both lists
        while (current1 != null || current2 != null) {
            int sum = (current1 == null ? 0 : current1.val) + (current2 == null ? 0 : current2.val);
            int carry = sum / 10;
            int remainder = sum % 10;

            currentSum.next = new ListNode(remainder);
            currentSum = currentSum.next;

            if (carry > 0) {
                currentSum.next = new ListNode(carry);
                currentSum = currentSum.next;
            }

            if (current1 != null) current1 = current1.next;
            if (current2 != null) current2 = current2.next;
        }

        // Return the head of the sum list
        return sumHead1.next;
    }

}
