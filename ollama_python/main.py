import ollama
response = ollama.chat(model='llama2', messages=[
  {
    'role': 'user',
    'content': """
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

/** see test {@link _001_TwoSum.PracticeTest } */
public class Practice {

    public int[] twoSum(int[] nums, int target) {
        // TODO Complete the implementation
        return null;
    }

}

    """
  },
])
print(response['message']['content'])