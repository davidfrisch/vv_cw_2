/**
 ***************************************************************************
 * Description:
 * Given an array of integers, find two numbers such that they add up to 
 * a specific target number. 
 * The function twoSum should return indices of the two numbers such that 
 * they add up to the target, where index1 must be less than index2. 
 * Please note that your returned answers (both index1 and index2) are not 
 * zero-based. 
 * 
 * You may assume that each input would have exactly one solution. 
 * Input: numbers={2, 7, 11, 15}, target=9 
 * Output: index1=1, index2=2
 * 
 ***************************************************************************
 * @tag : Array; Hash Table
 * {@link https://leetcode.com/problems/two-sum/ }
 */
package _001_TwoSum;

/** see test {@link _001_TwoSum.PracticeTest } */
import java.util.HashMap;


public class Practice {

        public int[] twoSum(int[] nums, int target) {
        // Map to store numbers and their indices
        HashMap<Integer, Integer> map = new HashMap<>();

        // Iterate through the array
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            // If complement exists in the map, return indices
            if (map.containsKey(complement)) {
                return new int[]{map.get(complement) + 1, i + 1}; // Indices are not zero-based
            }
            // Otherwise, put the current number and its index into the map
            map.put(nums[i], i);
        }
        // If no solution is found
        throw new IllegalArgumentException("No two sum solution");
    }

}
