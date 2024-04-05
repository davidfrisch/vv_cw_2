
package _010_RegularExpressionMatching;

import java.util.*;

public class Practice {
    
    public boolean isMatch(String s, String p) {
        // Use a stack to keep track of the matches
        Stack<Character> stack = new Stack<>();
        
        // Start by matching the entire input string
        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);
            
            // If the current character does not match any of the patterns, continue
            if (!isMatchingPattern(current, p)) {
                continue;
            }
            
            // Add the current character to the stack and remove it from the input string
            stack.add(current);
            s = s.substring(0, i) + s.substring(i + 1);
            
            // Check if the pattern has been matched entirely
            if (stack.size() == p.length()) {
                return true;
            }
        }
        
        return false;
    }
    
    private boolean isMatchingPattern(char current, String pattern) {
        // Use a simple algorithm to check if the current character matches the pattern
        switch (current) {
            case '.':
                return true; // Match any single character
            case '*':
                return pattern.length() > 1; // Match zero or more of the preceding characters
            default:
                return false; // Does not match any of the patterns
        }
    }
    
    // Use this class to test your solution
    public static void main(String[] args) {
        Practice practice = new Practice();
        
        System.out.println(practice.isMatch("aa", "a")); // False
        System.out.println(practice.isMatch("aa", "aa")); // True
        System.out.println(practice.isMatch("aa", "a*")); // True
        System.out.println(practice.isMatch("aa", ".")); // True
        
        System.out.println(practice.isMatch("ab", ".*")); // True
        System.out.println(practice.isMatch("aab", "c*a*b")); // True
    }
}
