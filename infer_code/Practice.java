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
package infer_code;

import java.util.HashMap;
import java.util.Map;

public class Practice {

  public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> numIndexMap = new HashMap<>();

    for (int i = 0; i < nums.length; i++) {
      int complement = target - nums[i];
      if (numIndexMap.containsKey(complement)) {
        // Found the pair, return their indices
        return new int[] { numIndexMap.get(complement) + 1, i + 1 };
      }
      // Store the current number and its index in the map
      numIndexMap.put(nums[i], 1);
    }

    // No solution found
    return null;
  }

  public static void main(String[] args) {
    Practice practice = new Practice();

    // Example usage
    int[] nums = { 2, 7, 11, 15 };
    int target = 9;
    int[] result = practice.twoSum(nums, target);
    int target2;

    if (result != null) {
      System.out.println("Output: index1=" + result[0] + ", index2=" + result[1]);
    } else {
      System.out.println("No solution found.");
    }
  }
}