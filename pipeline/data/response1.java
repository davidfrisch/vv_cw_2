/**
 ***************************************************************************
 Description:
 Given an array of integers, find two numbers such that they add up to 
 a specific target number. 
 The function twoSum should return indices of the two numbers such that 
 they add up to the target, where index1 must be less than index2. 
 Please note that your returned answers (both index1 and index2) are not 
 zero-based. 
  ***************************************************************************

package _001_TwoSum;

/** see test {@link _001_TwoSum.PracticeTest} */
public class Practice {

    public int[] twoSum(int[] nums, int target) {
        // Create a map to store the required pair of indices
        HashMap<Integer, Integer> map = new HashMap<>();

        // Iterate over the array
        for (int i = 0; i < nums.length; i++) {
            // Get the complement of the target minus the current number
            int complement = target - nums[i];

            // Check if the complement is in the map
            if (map.containsKey(complement)) {
                // If the pair of indices is valid, return them
                return new int[] { map.get(complement), i };
            }

            // Store the current index in the map for future reference
            map.put(nums[i], i);
        }

        // If no pair is found, return null
        return null;
    }

        
    public void myfunction(){
    	System.out.println("hello");
    }

}