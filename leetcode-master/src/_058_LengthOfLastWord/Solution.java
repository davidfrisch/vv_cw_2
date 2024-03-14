/**
 * Time : O(); Space: O()
 * @tag : String
 * @by  : Steven Cooks
 * @date: Jun 3, 2015
 *******************************************************************************
 * Description: 
 * 
 * Given a string s consists of upper/lower-case alphabets and empty space 
 * characters ' ', return the length of last word in the string. 
 * If the last word does not exist, return 0. 
 * 
 * Note: A word is defined as a character sequence consists of non-space 
 * characters only. 
 * 
 * For example, Given s = "Hello World", return 5.
 * 
 *******************************************************************************
 * {@link https://leetcode.com/problems/length-of-last-word/ }
 */
package _058_LengthOfLastWord;

/** see test {@link _058_LengthOfLastWord.SolutionTest } */
public class Solution {

    public int lengthOfLastWord(String s) {
        if (s.length() == 0) {
            return 0;
        }
        String[] parts = s.split(" ");
        return parts.length == 0 ? 0 : parts[parts.length - 1].length();
    }

}
